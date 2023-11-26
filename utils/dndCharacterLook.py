import streamlit as st

def select_character_look():
    # Initialize session states for look attributes if they don't exist
    attributes = {
        'sex': '',
        'age': '',
        'height': '',
        'weight': '',
        'physique': '',
        'eyes': '',
        'eye_color': '',
        'hair_style': '',
        'hair_color': '',
        'tattoos': False,
        'facial_war_paint': False,
        'ear_rings': False,
        'eye_patch': False
    }

    for attr, default in attributes.items():
        if attr not in st.session_state:
            st.session_state[attr] = default

    # Create UI elements for each attribute
    st.session_state['height'] = st.text_input("Height", st.session_state['height'])
    st.session_state['weight'] = st.text_input("Weight", st.session_state['weight'])
    st.session_state['physique'] = st.text_input("Physique Build", st.session_state['physique'])
    st.session_state['eyes'] = st.text_input("Eyes", st.session_state['eyes'])
    st.session_state['eye_color'] = st.text_input("Eye Color", st.session_state['eye_color'])
    st.session_state['hair_style'] = st.text_input("Hair Style", st.session_state['hair_style'])
    st.session_state['hair_color'] = st.text_input("Hair Color", st.session_state['hair_color'])
    st.session_state['tattoos'] = st.checkbox("Has Tattoos", st.session_state['tattoos'])
    st.session_state['facial_war_paint'] = st.checkbox("Has Facial War Paint", st.session_state['facial_war_paint'])
    st.session_state['ear_rings'] = st.checkbox("Has Ear Rings", st.session_state['ear_rings'])
    st.session_state['eye_patch'] = st.checkbox("Has Eye Patch", st.session_state['eye_patch'])
