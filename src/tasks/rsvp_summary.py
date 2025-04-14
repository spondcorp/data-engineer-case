from flytekit import task, FlyteFile, FlyteDirectory
import flytekit
from pyspark.sql import functions as F
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from flytekitplugins.spark import Spark


@task(
    task_config=Spark(
        spark_conf={
            "spark.master": "local[*]",
            "spark.executor.memory": "1g",
            "spark.driver.memory": "1g",
            "spark.sql.shuffle.partitions": "1",
            "spark.executor.cores": "2",
            "spark.executor.instances": "5",
        },
    )
)
def rsvp_summary(data_dir_path: FlyteDirectory, output_dir_path: str) -> str:
    spark_session: SparkSession = flytekit.current_context().spark_session
    rsvp_data_file = FlyteFile(f"{data_dir_path.path}/event_rsvps.csv")
    event_rsvps_df = spark_session.read.csv(rsvp_data_file.path, header=True)

    rsvp_summary = transform(event_rsvps_df)

    output_path = f"{output_dir_path}/rsvp_summary"
    rsvp_summary.write.mode("overwrite").csv(output_path, header=True)

    return output_path


def transform(rsvp_df: DataFrame) -> DataFrame:
    return (
        rsvp_df.withColumn("response_date", F.to_date("responded_at"))
        .groupBy("event_id", "response_date")
        .agg(
            F.sum(F.when(F.col("rsvp_status") == 1, 1).otherwise(0)).alias(
                "accepted_count"
            ),
            F.sum(F.when(F.col("rsvp_status") == 2, 1).otherwise(0)).alias(
                "declined_count"
            ),
            F.sum(F.when(F.col("rsvp_status") == 0, 1).otherwise(0)).alias(
                "unanswered_count"
            ),
        )
        .orderBy("event_id", "response_date")
    )
