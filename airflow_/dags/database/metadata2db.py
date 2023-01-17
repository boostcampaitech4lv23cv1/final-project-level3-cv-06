import pandas as pd
from sqlalchemy import create_engine


def df2db(keyword):
    user = "myuser"
    password = "mypassword"
    host = "localhost"
    port = 5432
    database = "airflow_db"

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
    print("connecting to db")
    df = pd.read_feather(f"dags/crawled_img/pixabay/metadata/{keyword}.feather")
    print("read feather file")
    df.to_sql(keyword, engine, if_exists="append", index=False)
    print(f"send {keyword} feather file to db")


if __name__ == "__main__":
    df2db(keyword="animal")
