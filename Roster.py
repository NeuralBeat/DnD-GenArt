import os
import streamlit as st
from main_menu import *
from utils.imageHandler import *
from utils.specifc_callbacks import *


def Roster():
    title_img = 'images/generic/DnDRoster.webp'
 
    ########## MAIN ###########

    spacer1, header_col, spacer2 = st.columns([1,1,1])

    with header_col:
        st.image(title_img, width=200)

    st.subheader("ROSTER OF ADVENTURERS")
    st.divider()

    # Get and display the sorted images
    image_files = get_sorted_images()
    for image_file in image_files:
        st.image(image_file, width = 275, caption=os.path.basename(image_file))
        st.divider()

    st.divider()
    st.button("RETURN TO MENU", key="return_main_from_chargen_2", on_click=update_return_to_main_menu)