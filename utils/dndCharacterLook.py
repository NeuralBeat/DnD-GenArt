import streamlit as st
from utils.dndRace import *

def select_character_look():
    #Intitialize default attributes
    default_sex = st.session_state.get('selected_sex', '')
    default_age = st.session_state.get('selected_age', '')
    default_physique = st.session_state.get('selected_physique', '')
    default_skin_color = st.session_state.get('selected_age', '')
    default_scale_color = st.session_state.get('selected_age', '')
    default_skin_taint = st.session_state.get('selected_age', '')
    default_hair_color = st.session_state.get('selected_age', '')
    default_hair_length = st.session_state.get('selected_age', '')
    default_hair_style_short = st.session_state.get('selected_age', '')
    default_hair_style_long = st.session_state.get('selected_age', '')
    default_beard_style = st.session_state.get('selected_age', '')
    default_accessory  = st.session_state.get('selected_accessories', '')
    default_tattoo = st.session_state.get('selected_tattoo', '')

    #Initialize default attribute acitvation states
    default_hair_activation = st.session_state.get('hair_activation', False)
    default_beard_activation = st.session_state.get('beard_activation', False)
    default_tattoo_activation = st.session_state.get('tattoo_activation', False)
    default_accessory_activation = st.session_state.get('accessories_activation', False)

    # Mappings for attributes
    sexes = {1: 'Male', 2: 'Female'}
    ages = {1: 'Young', 2: 'Adult', 3: 'Seasoned', 4: 'Old'}
    physiques = {1: 'Gaunt', 2: 'Slim', 3: 'Average', 4: 'Athletic', 5: 'Muscular', 6: 'Heavy'}
    skin_colors = {1: 'white', 2:'brown', 3:'black', 4:'red', 5:'yellow', 6:'grey', 7:'green', 8:'purple'}
    scale_colors = {1: 'black', 2:'blue', 3:'green', 4:'red', 5:'white', 6:'bronze', 7:'silver', 8:'gold'}
    skin_taint = {1: 'pale', 2: 'brown', 3: 'grey', 4: 'red', 5: 'green'}
    hair_colors = {1: 'Black', 2: 'Brown', 3: 'Blonde', 4: 'Red', 5: 'Grey', 6: 'White'}
    eye_colors = {1: 'Brown', 2: 'Blue', 3: 'Green', 4: 'Grey', 5: 'Red', 6:'Purple'}
    hair_length = {1: 'short', 3: 'long'}
    hair_style_short = {1: 'crew cut', 2:'slicked back style', 3: 'pixie cut', 4:'short pomp', 5: 'undercut', 6:'mohawk', 7:'skin fade', 8:'mid fade taper cut', 9:'buzz cut', 10:'high & tight'}
    hair_style_long = {1:'natural long', 2:'french braid', 3:'chignon', 4:'ponytail', 5:'braid', 6:'dreadlocks', 7:'curls', 8:'fishtail hair', 9:'surfer hair', 10:'hime cut'}
    beard_style = {1: 'None', 2:'stubble', 3:'mustache', 4:'classic full beard', 5:'goatee', 6:'horseshoe', 7:'mutton chops', 8:'brett', 9:'braided beard', 10:'old dutch'}
    accessories = {1: 'nose rings', 2:'ear rings', 3:'eye patch', 4:'scars', 5:'bandana', 6:'war paint', 7: 'glasses', 8:'monocle'}
    tattoos = {1:'tribal', 2:'mythical', 3:'runic', 4:'norse', 5:'skull', 6: 'infernal', 7:'demonic', 8:'religious'}

    # Sliders for selection
    selected_sex = st.radio("Select Sex", options=list(sexes.values()))
    selected_age = st.select_slider("Select Age", options=list(ages.values()))
    selected_physique = st.select_slider("Select Physique Build", options=list(physiques.values()))
    selected_eye_color = st.select_slider("Select Eye Color", options=list(eye_colors.values()))

    if st.session_state['selected_race'] == 'Dragonborn':
        selected_scale_color = st.select_slider("Select Scale Color", options=list(scale_colors.values()))
    
    else:
        selected_skin_color = st.select_slider("Select Skin Color", options=list(skin_colors.values()))
        selected_skin_taint = st.select_slider("Select Taint", options=list(skin_taint.values()))

        hair_activation = st.toggle("Hair", value=default_hair_activation, key="hair_activation")
        if hair_activation == True:
            selected_hair_length = st.selectbox("Select Hair Length", options=list(hair_length.values()))
            selected_hair_color = st.select_slider("Select Hair Color", options=list(hair_colors.values()))
            if selected_hair_length == 'short':
                selected_hair_style_short = st.select_slider("Select Short Hair Style", options=list(hair_style_short.values()))
            else:
                selected_hair_style_long = st.select_slider("Select Long Hair Style", options=list(hair_style_long.values()))
        

        beard_activation = st.toggle("Bearded", value=default_beard_activation, key="beard_activation")
        if beard_activation == True:
            selected_beard_style = st.select_slider("Select Beard Style", options=list(beard_style.values()))   
    
    tattoo_activation = st.toggle("Tattoo", value=default_tattoo_activation, key="tattoo_activation")
    if tattoo_activation == True:
        selected_tattoo_style = st.select_slider("Select Tattoo Style", options=list(tattoos.values()))

    accessories_activation = st.toggle("Accessories", value=default_accessory_activation, key="accessories_activation")
    if accessories_activation == True:    
        selected_accessories = st.select_slider("Select Accessories", options=list(accessories.values()))

