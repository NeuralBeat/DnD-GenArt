import os
import base64
import streamlit as st
from st_clickable_images import clickable_images
from main_menu import *
from utils.imageHandler import *
from utils.specifc_callbacks import *

def Roster():
    # Directory containing the character portraits
    portraits_dir = 'history/Portraits'
    portrait_files = sorted([file for file in os.listdir(portraits_dir) if file.endswith('.webp')], reverse=True)

    # Initialize current portrait index in session state
    if 'current_portrait_index' not in st.session_state:
        st.session_state['current_portrait_index'] = 0
    
    # Initialize click flags
    if 'left_clicked' not in st.session_state:
        st.session_state['left_clicked'] = False
    if 'right_clicked' not in st.session_state:
        st.session_state['right_clicked'] = False
    
    title_img = 'images/generic/DnDRoster.webp'
 
    ########## MAIN ###########

    spacer1, header_col, spacer2 = st.columns([1,1,1])

    #with header_col:
        #st.image(title_img, width=200)

    st.subheader("ROSTER OF ADVENTURERS")
    st.divider()

    lButton_col, Portrait_col, rButton_col = st.columns([1,2,1])

    with Portrait_col:
        # Display the current portrait
        current_portrait = portrait_files[st.session_state['current_portrait_index']]
        current_portrait_path = os.path.join(portraits_dir, current_portrait)
        st.image(current_portrait_path, width = 250, use_column_width=True)

    # Left Navigation Button
    with lButton_col:
        lButton_absPath = get_absolute_path('images/generic/NavigatorButtonLeft.webp')
        left_button = get_image_as_base64(lButton_absPath)
        if clickable_images(
        [left_button],
        titles=["PREVIOUS IN ROSTER"],
        img_style={"height": "550px"},
        key='previous_roster_image_button'
        ):
            handle_left_click(portrait_files)

    # Right Navigation Button
    with rButton_col:
        rButton_absPath = get_absolute_path('images/generic/NavigatorButtonRight.webp')
        right_button = get_image_as_base64(rButton_absPath)
        if clickable_images(
        [right_button],
        titles=["NEXT IN ROSTER"],
        img_style={"height": "550px"},
        key='next_roster_image_button'
        ): 
            handle_right_click(portrait_files)
    
    st.divider()
    st.button("RETURN TO MENU", key="return_main_from_chargen_2", on_click=update_return_to_main_menu)

    if st.session_state['left_clicked']:
        st.session_state['left_clicked'] = False
    
    if st.session_state['right_clicked']:
        st.session_state['right_clicked'] = False

def handle_left_click(portrait_files):
    st.session_state['current_portrait_index'] = (st.session_state['current_portrait_index'] - 1) % len(portrait_files)
    st.session_state['left_clicked'] = True

def handle_right_click(portrait_files):
    st.session_state['current_portrait_index'] = (st.session_state['current_portrait_index'] + 1) % len(portrait_files)
    st.session_state['right_clicked'] = True