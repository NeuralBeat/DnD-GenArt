import streamlit as st

if 'selected_class' not in st.session_state:
    st.session_state['selected_class'] = 'Select a class'

if 'selected_subclass' not in st.session_state:
    st.session_state['selected_subclass'] = None