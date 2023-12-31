import streamlit as st
from utils.dndRace import *

def select_character_look():
    #Intitialize default attributes
    default_name = st.session_state.get('selected_name', '')
    default_sex = st.session_state.get('selected_sex', 'Male')
    default_age = st.session_state.get('selected_age', 'Adult')
    default_physique = st.session_state.get('selected_physique', 'Average')
    default_skin_color = st.session_state.get('selected_skin_color', '')
    default_scale_color = st.session_state.get('selected_scale_color', '')
    default_skin_taint = st.session_state.get('selected_skin_taint', '')
    default_hair_color = st.session_state.get('selected_hair_color', '')
    default_hair_length = st.session_state.get('selected_hair_length', '')
    default_hair_style_short = st.session_state.get('selected_hair_style_short', '')
    default_hair_style_long = st.session_state.get('selected_hair_style_long', '')
    default_beard_style = st.session_state.get('selected_beard_style', '')
    default_accessory  = st.session_state.get('selected_accessories', '')
    default_tattoo = st.session_state.get('selected_tattoo', '')


    #Initialize default attribute acitvation states
    default_hair_activation = st.session_state.get('hair_activation', False)
    default_beard_activation = st.session_state.get('beard_activation', False)
    default_tattoo_activation = st.session_state.get('tattoo_activation', False)
    default_accessory_activation = st.session_state.get('accessories_activation', False)
    default_horns_activation = st.session_state.get('horns_activation', False)

    # Mappings for attributes
    sexes = {1: 'Male', 2: 'Female'}
    ages = {1: 'Young', 2: 'Adult', 3: 'Seasoned', 4: 'Old'}
    physiques = {1: 'Gaunt', 2: 'Slim', 3: 'Average', 4: 'Athletic', 5: 'Muscular', 6: 'Heavy'}
    skin_colors = {1: 'white', 2:'brown', 3:'black', 4:'red', 5:'yellow', 6:'blue', 7:'green', 8:'purple', 9:'grey'}
    scale_colors = {1: 'black', 2:'blue', 3:'green', 4:'red', 5:'white', 6:'bronze', 7:'silver', 8:'gold'}
    skin_taint = {1: 'pale', 2: 'brown', 3: 'grey', 4: 'red', 5: 'green', 6: 'blue', 7: 'dark'}
    hair_colors = {1: 'Black', 2: 'Brown', 3: 'Blonde', 4: 'Red', 5: 'Grey', 6: 'White'}
    eye_colors = {1: 'Brown', 2: 'Blue', 3: 'Green', 4: 'Grey', 5: 'Red', 6:'Purple'}
    hair_length = {1: 'short', 3: 'long'}
    horns_style = {1: 'goat', 2: 'bovine', 3: 'lizard', 4:'antelope', 5: 'devil', 6: 'demon', 7: 'draconic', 8:'triceratops'}
    hair_style_short = {1: 'crew cut', 2:'slicked back style', 3: 'pixie cut', 4:'short pomp', 5: 'undercut', 6:'mohawk', 7:'skin fade', 8:'mid fade taper cut', 9:'buzz cut', 10:'high & tight'}
    hair_style_long = {1:'natural long', 2:'french braid', 3:'chignon', 4:'rose braid', 5:'braid', 6:'dreadlocks', 7:'curls', 8:'fishtail hair', 9:'surfer hair', 10:'hime cut'}
    beard_style = {1: 'stubble', 2:'fu manchu', 3:'mustache', 4:'classic full beard', 5:'goatee', 6:'horseshoe', 7:'mutton chops', 8:'brett', 9:'braided beard', 10:'old dutch'}
    accessories = {1: 'nose rings', 2:'ear rings', 3:'eye patch', 4:'scars', 5:'heterochromia', 6:'war paint', 7: 'glasses', 8:'monocle'}
    tattoos = {1:'tribal', 2:'mythical', 3:'runic', 4:'norse', 5:'skull', 6: 'infernal', 7:'demonic', 8:'religious'}

    selected_sex = st.radio("SELECT SEX", options=list(sexes.values()), key='selected_sex', horizontal=True)
    # Use columns to split the layout
    col1, col2 = st.columns(2)

    # Sliders for selection
    with col1:
        selected_age = st.select_slider("SELECT AGE", options=list(ages.values()), key='selected_age')
        if st.session_state['selected_race'] == 'Dragonborn':
            selected_scale_color = st.select_slider("SELECT SCALE COLOR", options=list(scale_colors.values()), key='selected_scale_color')
        if st.session_state['selected_race'] != 'Dragonborn':
            selected_skin_color = st.select_slider("SELECT SKIN COLOR", options=list(skin_colors.values()), key='selected_skin_color')
    
        
    with col2:
        selected_physique = st.select_slider("SELECT PHYSIQUE", options=list(physiques.values()), key='selected_physique')
        selected_eye_color = st.select_slider("SELECT EYE COLOR", options=list(eye_colors.values()), key='selected_eye_color') 
        if st.session_state['selected_race'] != 'Dragonborn':
            selected_skin_taint = st.select_slider("SELECT TAINT", options=list(skin_taint.values()), key='selected_skin_taint')

    if st.session_state['selected_race'] == 'Dragonborn' or 'Tiefling':
        horns_activation = st.toggle("Horns", value=default_horns_activation, key='horns_activation')
        if horns_activation==True:
            selected_horns_style = st.select_slider("SELECT HORN STYLE", options=list(horns_style.values()), key='selected_horns_style')
    
    if st.session_state['selected_race'] != 'Dragonborn':
        hair_activation = st.toggle("HAIR", value=default_hair_activation, key="hair_activation")
        if hair_activation == True:
            selected_hair_length = st.selectbox("SELECT HAIR LENGTH", options=list(hair_length.values()), key='selected_hair_length')
            selected_hair_color = st.select_slider("SELECT HAIR COLOR", options=list(hair_colors.values()), key='selected_hair_color')
            if selected_hair_length == 'short':
                selected_hair_style_short = st.select_slider("SELECT SHORT HAIR STYLE", options=list(hair_style_short.values()), key='selected_hair_style_short')
            else:
                selected_hair_style_long = st.select_slider("SELECT LONG HAIR STYLE", options=list(hair_style_long.values()), key='selected_hair_style_long')
    
        beard_activation = st.toggle("BEARDED", value=default_beard_activation, key="beard_activation")
        if beard_activation == True:
            selected_beard_style = st.select_slider("SELECT BEARD STYLE", options=list(beard_style.values()), key='selected_beard_style')   
    
    tattoo_activation = st.toggle("TATTOO", value=default_tattoo_activation, key="tattoo_activation")
    if tattoo_activation == True:
        selected_tattoo_style = st.select_slider("SELECT TATTOO STYLE", options=list(tattoos.values()), key='selected_tattoo_style')

    accessories_activation = st.toggle("ACCESSORIES", value=default_accessory_activation, key="accessories_activation")
    if accessories_activation == True:    
        selected_accessories = st.select_slider("SELECT ACCESSORIES", options=list(accessories.values()), key='selected_accessories')


def select_name():
        default_name = st.session_state.get('selected_name', '')

        selected_name = st.text_input("CHARACTER NAME", key='selected_name')

def select_level():
    default_level = st.session_state.get('selected_level', 1)

    selected_level = st.number_input('LEVEL', 1, 20, key='selected_level')