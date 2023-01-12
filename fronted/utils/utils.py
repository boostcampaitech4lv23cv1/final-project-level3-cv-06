import streamlit as st
from time import sleep

def change_game_start_session():
    st.session_state.game_start = not st.session_state.game_start

    
    