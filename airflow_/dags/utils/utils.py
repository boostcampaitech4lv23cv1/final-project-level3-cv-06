import pandas as pd
import pyarrow as pa
import pyarrow.feather as feather
import requests
import yaml


def read_yaml(AIRFLOW_HOME):
    with open(f"{AIRFLOW_HOME}/secret.yml", "r") as f:
        secret = yaml.load(f, Loader=yaml.FullLoader)
    return secret


def send_data2api(
    logger, KEYWORD: str, secret: yaml, df: pd.DataFrame, method: str
) -> None:
    """send data to api by method

    Args:
        df (pd.DataFrame): metadata dataframe
    """
    url = f"{secret['api_url']}/api/v1/meta/{method}"

    buffer = pa.BufferOutputStream()
    feather.write_feather(df, buffer)

    file = {"file": buffer.getvalue().to_pybytes()}
    category = {"category": KEYWORD}

    try:
        res = requests.post(url, files=file, data=category)
    except Exception as err:
        logger.warning(err)
        logger.warning("an error occured sending feather file to api")

    # Check the status code of the response
    try:
        res.raise_for_status()
    except Exception as e:
        logger.warning(e)
