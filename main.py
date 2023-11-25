import streamlit as st
import os
import glob
from utils.dndClass import *


side_bar_img = "https://i.pinimg.com/564x/05/c1/5a/05c15aca14964af944aac1c638e1d7d2.jpg"

##### START WITH APP LAYOUT ######

st.set_page_config(page_title="DnD Disguise", page_icon="https://i.pinimg.com/564x/05/c1/5a/05c15aca14964af944aac1c638e1d7d2.jpg")

##### INIT SESSION STATES ####
if 'selected_class' not in st.session_state:
    st.session_state['selected_class'] = 'Select a class'

if 'selected_subclass' not in st.session_state:
    st.session_state['selected_subclass'] = None


########### NAVIGATIONBAR ###########

with st.sidebar:
    st.image(side_bar_img, use_column_width=True)
    st.title("DnD Disguise")
    st.info("This application automatically generates character portraits based on the selected attributes using AI.")

########## MAIN ###########

st.title("D&D DISGUISE")
st.subheader("AI-SUPPORTED CHARACTER ART", anchor=None)

st.session_state['selected_class'] = st.selectbox(
    'Select your Class', 
    classes, 
    index=classes.index(default_class),
    key='class_selector'
)

# Update subclass state based on class selection
if st.session_state['selected_class'] in subclasses:
    st.session_state['selected_subclass'] = st.selectbox(
        'Select your Subclass', 
        subclasses[st.session_state['selected_class']],
        index=0 if default_subclass not in subclasses[st.session_state['selected_class']] else subclasses[st.session_state['selected_class']].index(default_subclass),
        key='subclass_selector'
    )
else:
    st.session_state['selected_subclass'] = ''