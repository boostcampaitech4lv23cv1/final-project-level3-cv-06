import os
import shutil
import sys

KEYWORD, SITE, SCRAPED_TIME = sys.argv[1:]

AIRFLOW_HOME = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
)


def remove_dirs():
    base_path = f"{AIRFLOW_HOME}/classification/data"
    path = os.path.join(base_path, KEYWORD, SITE, SCRAPED_TIME)
    shutil.rmtree(path)
