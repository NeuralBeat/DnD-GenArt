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

    # Mappings for attributes
    sexes = {1: 'Male', 2: 'Female', 3: 'Other'}
    ages = {1: 'Young', 2: 'Seasoned', 3: 'Old'}
    physiques = {1: 'Slim', 2: 'Average', 3: 'Athletic', 4: 'Muscular', 5: 'Heavy'}
    skin_colors = {1: 'white', 2:'brown', 3:'black', 4:'red', 5:'yellow', 6:'grey', 7:'green', 8:'purple'}
    scale_colors = {1: 'black', 2:'blue', 3:'green', 4:'red', 5:'white', 6:'bronze', 7:'silver', 8:'gold'}
    taint = {1: 'pale', 2: 'brown', 3: 'grey', 4: 'red', 5: 'green'}
    hair_colors = {1: 'Black', 2: 'Brown', 3: 'Blonde', 4: 'Red', 5: 'Grey', 6: 'White'}
    eye_colors = {1: 'Brown', 2: 'Blue', 3: 'Green', 4: 'Grey', 5: 'Red', 6:'Purple'}
    hair_style = {1: 'bald', 2: 'short', 3: 'medium', 4: 'long'}
    


    # Sliders for selection
    selected_hair_color = st.select_slider("Select Hair Color", options=list(hair_colors.values()))
    selected_eye_color = st.select_slider("Select Eye Color", options=list(eye_colors.values()))
    selected_physique = st.select_slider("Select Physique Build", options=list(physiques.values()))
    selected_sex = st.select_slider("Select Sex", options=list(sexes.values()))

    for attr, default in attributes.items():
        if attr not in st.session_state:
            st.session_state[attr] = default

    # Create UI elements for each attribute
    st.session_state['sex'] = st.toggle("Sex", st.session_state['sex'])
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
