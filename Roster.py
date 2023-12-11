import os
import streamlit as st
from main_menu import *
from utils.imageHandler import *
from utils.specifc_callbacks import *


def Roster():
    st.subheader("IMAGE TIMELINE")
    st.divider()

    # Get and display the sorted images
    image_files = get_sorted_images()
    for image_file in image_files:
        st.image(image_file, width = 275, caption=os.path.basename(image_file))
        st.divider()

    st.button("RETURN TO MENU", key="return_main_from_chargen_2", on_click=update_return_to_main_menu)