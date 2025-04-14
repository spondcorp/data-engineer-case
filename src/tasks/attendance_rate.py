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
        },
    )
)
def attendance_rate(data_dir_path: FlyteDirectory, output_dir_path: str) -> str:
    pass


def transform():
    pass
