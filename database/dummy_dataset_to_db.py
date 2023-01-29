import os
import time
from argparse import ArgumentParser
from glob import glob

import pandas as pd
import psycopg2
from PIL import Image


def dummy_dataset_to_df():
    """dataset directory에 있는 이미지의 정보를 df 형식으로 변환
    Args:
    Returns:
        pd.DataFrame: 이미지의 정보를 포함
    """
    original_file_paths = glob("../dataset/original/**/*.*", recursive=True)
    dataset_list = []
    for i in original_file_paths:

        img = Image.open(i)
        img_width, img_height = img.size

        original_fn = os.path.basename(i)
        processed_file_path_split = i.split("/")

        category = processed_file_path_split[3]
        label = processed_file_path_split[4]

        processed_file_path_split[2] = "processed"
        processed_file_path = os.path.join(*processed_file_path_split)
        processed_file_paths = glob(os.path.splitext(processed_file_path)[0] + ".*")
        if len(processed_file_paths) == 1:
            processed = True
            processed_fn = os.path.basename(processed_file_paths[0])
        else:
            processed = False
            processed_fn = None
        dataset_list.append(
            [
                category,
                label,
                img_height,
                img_width,
                original_fn,
                processed_fn,
                processed,
            ]
        )
    df = pd.DataFrame(
        dataset_list,
        columns=[
            "category",
            "label",
            "img_height",
            "img_width",
            "original_fn",
            "processed_fn",
            "processed",
        ],
    )
    return df


def insert_data(db_connect: psycopg2.extensions.connection, df: pd.DataFrame):
    """dataset directory에 있는 이미지의 정보를 df 형식으로 변환
    Args:
        db_connect (psycopg2.extensions.connection): PostgreSQL과의 connection
        df (pd.DataFrame): database에 삽입할 pd.DataFrame
    Returns:
    """
    for i in range(len(df)):
        data = df.iloc[i]
        insert_row_query = f"""
        INSERT INTO savepaint_img_data
            (timestamp, category, label, img_height, img_width, original_fn, processed_fn, processed)
            VALUES (
                NOW(),
                '{data.category}',
                '{data.label}',
                {data.img_height},
                {data.img_width},
                '{data.original_fn}',
                '{data.processed_fn}',
                '{data.processed}'
            );
        """
        with db_connect.cursor() as cur:
            cur.execute(insert_row_query)
            db_connect.commit()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--db-host", dest="db_host", type=str, default="localhost")
    args = parser.parse_args()

    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host=args.db_host,
        port=5432,
        database="mydatabase",
    )

    df = dummy_dataset_to_df()
    insert_data(db_connect, df)
