import streamlit as st
import os
import glob
from utils.dndClass import *


side_bar_img = "https://i.pinimg.com/564x/05/c1/5a/05c15aca14964af944aac1c638e1d7d2.jpg"

##### START WITH APP LAYOUT ######

st.set_page_config(page_title="DnD Disguise", page_icon="https://i.pinimg.com/564x/05/c1/5a/05c15aca14964af944aac1c638e1d7d2.jpg")

########### NAVIGATIONBAR ###########

with st.sidebar:
    st.image(side_bar_img, use_column_width=True)
    st.title("DnD Disguise")
    st.info("This application automatically generates character portraits based on the selected attributes using AI.")

########## MAIN ###########

st.title("D&D DISGUISE")
st.subheader("AI-SUPPORTED CHARACTER ART", anchor=None)

select_class()