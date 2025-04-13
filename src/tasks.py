from flytekit import task
import psycopg2


@task
def extract_from_rdbms(
    db_host: str, db_port: int, db_name: str, start_date: str, end_date: str
) -> str:
    # Assumption(s):
    # Data extracted from the given table fits in memory
    # If it does not then we can mitigate this issue by
    # using "dynamic workflow" feature of Flyte which allows us to
    # create mutliple instances of this task and each instance can fetch a chunk of data
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user="postgres",
        password="password",
    )
    connection.close()
    return "Data extracted from RDBMS"
