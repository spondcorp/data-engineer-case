from flytekit import task, FlyteFile, FlyteDirectory
import flytekit
from pyspark.sql import functions as F
from pyspark.sql import DataFrame
from flytekitplugins.spark import Spark
from pyspark.sql import SparkSession


@task(
    task_config=Spark(
        spark_conf={
            "spark.master": "local[*]",
        },
    )
)
def daily_active_teams(data_dir_path: FlyteDirectory, output_dir_path: str) -> str:
    spark_session: SparkSession = flytekit.current_context().spark_session
    events_data_path = FlyteFile(f"{data_dir_path.path}/events.csv")
    print(f"events_data_path: {events_data_path.path}")
    events_data = spark_session.read.csv(events_data_path.path, header=True)

    daily_active_teams_data = transform(events_data)

    output_path = f"{output_dir_path}/daily_active_teams"
    daily_active_teams_data.write.mode("overwrite").csv(output_path, header=True)

    return output_path


def transform(events_data: DataFrame) -> DataFrame:
    daily_active_teams_data = (
        events_data.withColumnRenamed("event_start", "event_date")
        .withColumn("event_date", F.to_date("event_date"))
        .groupBy("event_date")
        .agg(
            F.countDistinct("team_id").alias("daily_active_team_count"),
        )
    )
    return daily_active_teams_data
