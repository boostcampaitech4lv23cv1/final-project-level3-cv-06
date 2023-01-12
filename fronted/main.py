from time import time, sleep
import streamlit as st
import requests
import threading

from utils import *

def main():
    st.set_page_config(layout='wide')

    set_session()

    with st.sidebar:
        category = st.selectbox('choose category', options=GAME_CATEGORIES)
        
    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        st.title('game title')
        if not st.session_state.game_start:
            st.button("Start", on_click=change_game_start_session)
    with col3:
        pass


    col1, col2, col3 = st.columns(3)

    with col1:
        pass
    with col2:
        if st.session_state.game_start:
            
            # progress bar
            
            # get image
            
            response = get_image(category)
            image = response["image"]
            label = response["label"]
            origin = response["origin_image"]
            st.markdown(
                f'<img src="data:image/gif;base64,{image}" alt="gif">',
                unsafe_allow_html=True,
            )
            
            
            st.button("Fin", on_click=reset_game)
    with col3:
        pass
    
    user_input = st.text_input(label='정답을 입력하세요')
    
    
    
    

    
if __name__ == '__main__':
    main()




