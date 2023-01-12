import streamlit as st

SESSION_VAR = {
    'game_start': False,
    'timer': 100
}

GAME_CATEGORIES = [
    'animals',
    'landmark'
]

def set_session():
    for session, value in SESSION_VAR.items():
        if session not in st.session_state:
            st.session_state[session] = value
    
# 초기화
def reset_game():
    for session, value in SESSION_VAR.items():
        st.session_state[session] = value

    