import pytest

from src.tasks import extract_from_rdbms


def test_extract_from_rdbms_task():
    extract_from_rdbms(
        db_host="localhost",
        db_port=5432,
        db_name="db_name",
        start_date="2023-01-01",
        end_date="2023-01-31",
    )
    pytest.fail("not implemented yet")
