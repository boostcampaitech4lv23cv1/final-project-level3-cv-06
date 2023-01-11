import requests

def get_image():
    params = {"info": "animal"}
    response = requests.post(f"http://127.0.0.1:8000", params=params).json()
    image_list.append(response["image"])
    ans_list.append(response["label"])
