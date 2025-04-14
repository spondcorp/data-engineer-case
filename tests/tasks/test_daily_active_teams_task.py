from datetime import date
import pytest
from pyspark.sql import SparkSession
from src.tasks.daily_active_teams import transform


@pytest.fixture(scope="module")
def spark():
    spark_session = (
        SparkSession.builder.appName("PySparkUnitTest").master("local[*]").getOrCreate()
    )
    yield spark_session
    spark_session.stop()


def test_daily_active_teams_transform(spark):
    input_data = [
        (
            "event_id_11",
            "team_id_1",
            "2025-04-14T19:30:00.000Z",
            "2024-04-14T20:30:00.000Z",
            51.45991,
            -2.5627005,
            "2025-04-14T16:22:33.794Z",
        ),
        (
            "event_id_12",
            "team_id_1",
            "2025-04-13T19:30:00.000Z",
            "2024-04-13T20:30:00.000Z",
            51.45991,
            -2.5627005,
            "2025-04-13T16:22:33.794Z",
        ),
        (
            "event_id_12",
            "team_id_2",
            "2025-04-13T19:30:00.000Z",
            "2024-04-13T20:30:00.000Z",
            51.45991,
            -2.5627005,
            "2025-04-12T16:22:33.794Z",
        ),
        (
            "event_id_22",
            "team_id_2",
            "2025-04-12T19:30:00.000Z",
            "2024-04-12T20:30:00.000Z",
            51.45991,
            -2.5627005,
            "2025-04-12T16:22:33.794Z",
        ),
    ]
    columns = [
        "event_id",
        "team_id",
        "event_start",
        "event_end",
        "latitude",
        "longitude",
        "created_at",
    ]
    events_data = spark.createDataFrame(input_data, columns)
    daily_active_teams = transform(events_data)
    daily_active_teams.show(truncate=False)
    expected_data = [
        (date(2025, 4, 14), 1),
        (date(2025, 4, 13), 2),
        (date(2025, 4, 12), 2),
    ]
    expected_columns = ["event_date", "daily_active_team_count"]
    expected_df = spark.createDataFrame(expected_data, expected_columns)
    __assert_dataframes(daily_active_teams, expected_df)


def __assert_dataframes(actual, expected):
    assert actual.count() == expected.count()
    assert actual.columns == expected.columns
    for col in actual.columns:
        assert (
            actual.select(col).distinct().collect()
            == expected.select(col).distinct().collect()
        )
