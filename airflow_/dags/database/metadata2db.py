import os

import pandas as pd
from sqlalchemy import create_engine

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")


def df2db(scraped_time,keyword, site):
    user = "airflow"
    password = "airflow"
    host = "postgres"
    port = 5432
    database = "airflow"

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
    print("connecting to db")
    df = pd.read_feather(
        f"{AIRFLOW_HOME}/dags/data/{keyword}/{site}/{scraped_time}/metadata.feather"
    )
    print("read feather file")
    df.to_sql(keyword, engine, if_exists="append", index=False)
    print(f"send {keyword}/{site} feather file to db")


if __name__ == "__main__":
    df2db(keyword="animal", site="pixabay")
# TODO airflow로 여러번 실행되었을때도 DB에 중복값이 없도록
