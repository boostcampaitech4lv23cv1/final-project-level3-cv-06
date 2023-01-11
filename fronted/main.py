import streamlit as st
import streamlit.components.v1 as components
import time
import requests
import concurrent.futures
from multiprocessing import Process, Queue

st.header("Demo version")
game_start = st.button("START")


def get_image():
    params = {"info": "animal"}
    response = requests.post(f"http://127.0.0.1:8000", params=params).json()
    image_list.append(response["image"])
    ans_list.append(response["label"])
    return


if game_start:
    image_list, ans_list = [], []
    get_image()
    st.markdown(
        f'<img src="data:image/gif;base64,{image_list[0]}" alt="gif">',
        unsafe_allow_html=True,
    )
