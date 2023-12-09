import streamlit as st

def update_return_to_main_menu():
    st.session_state['selected_page'] = 'main_menu'
