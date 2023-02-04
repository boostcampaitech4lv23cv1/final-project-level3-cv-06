import os

import pandas as pd
from google.cloud import storage, vision

os.environ["GCLOUD_PROJECT"] = "CV-NOOPS"


def detect_landmarks_uri(bucket_name, file_names) -> list:
    """Detects landmarks in the file located in Google Cloud Storage or on the
    Web."""
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    for file_name in file_names:
        image.source.image_uri = f"gs://{bucket_name}/{file_name}"

        response = client.landmark_detection(image=image)
        landmarks = response.landmark_annotations
        print("Landmarks:")

        for landmark in landmarks:
            print(landmark.description)

        if response.error.message:
            raise Exception(f"{response.error.message})")


if __name__ == "__main__":
    client = storage.Client()
    dir_name = 123  # TODO
    bucket_name = "scraped-img"
    bucket = client.get_bucket(bucket_name)
    blobs = list(bucket.list_blobs(prefix=dir_name))
    file_names = [blob.split(",")[1].strip() for blob in blobs]
    detect_landmarks_uri(bucket_name, file_names)
