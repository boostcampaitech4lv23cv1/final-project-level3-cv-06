import requests

def get_image(category: str):
    params = {"info": "animal"}
    response = requests.post(f"http://127.0.0.1:8000", params=params).json()
    return response
    
