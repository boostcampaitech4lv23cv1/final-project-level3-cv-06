from minio import Minio
from glob import glob
import os

BUCKET_NAME = "savepaint-bucket"

DATASET_ROOT_DIR = "../dataset"

client = Minio(
    "localhost:9000",
    access_key="minio", secret_key="miniostorage", secure=False
)

if not client.bucket_exists(BUCKET_NAME):
    client.make_bucket(BUCKET_NAME)


def upload_local_directory_to_minio(local_path: str, bucket_name: str, minio_path: str):
    """local_path 및 하위 directory, file들을 저장
    Args:
        local_path (str): bucket에 저장할 directory
        bucket_name (str): bucket name
        minio_path (str): minio path
    Returns:
    """
    assert os.path.isdir(local_path)

    for local_file in glob(local_path + '/**'):
        local_file = local_file.replace(os.sep, "/") # Replace \ with / on Windows
        if not os.path.isfile(local_file):
            upload_local_directory_to_minio(
                local_file, bucket_name, minio_path + "/" + os.path.basename(local_file))
        else:
            remote_path = os.path.join(
                minio_path, local_file[1 + len(local_path):])
            remote_path = remote_path.replace(
                os.sep, "/")  # Replace \ with / on Windows
            client.fput_object(bucket_name, remote_path, local_file)

upload_local_directory_to_minio(DATASET_ROOT_DIR, BUCKET_NAME, "")