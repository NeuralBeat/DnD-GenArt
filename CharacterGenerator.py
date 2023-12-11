import streamlit as st
import os
from utils.specifc_callbacks import *
from utils.dndClass import *
from utils.dndRace import *
from utils.dndAlignment import *
from utils.dndCharacterLook import *
from utils.promptCreator import *
from utils.imageHandler import *
from utils.attributeHandler import *
from utils.styleCSS import *

def CharacterGenerator():

    title_img = 'images/generic/DnDMask.webp'
 
    ########## MAIN ###########

    spacer1, header_col, spacer2 = st.columns([1,1,1])

    #with header_col:
    #    st.image(title_img, width=200)

    st.subheader("D&D CHARACTER GENERATOR", anchor=None)

    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["CORE", "ATTRIBUTES", "OPTICS", "SKILLS & TRAITS", "ARSENAL", "PORTRAIT", "SUMMARY"])

    # Tab 1: Core Attributes (Class, Race, Alignment)
    with tab1:
        # Call your function for selecting class, race, and alignment
        col1, col2 = st.columns(2)
        with col1:
            select_name()
        with col2:
            select_level()
        select_race()
        select_class()

    with tab2:
        select_attributes()

    # Tab 2: Optics (Character Look)
    with tab3:
        select_character_look()

    # Tab 3: Equipment & Arsenal
    with tab4:
        pass

    with tab5:
        pass

    with tab6:
        # Display the prompt
        if st.button("GENERATE CHARACTER IMAGE"):
            dalle_prompt = create_dalle_prompt()


            with st.spinner('GENERATING PORTRAIT ...'):
                image_url = generate_image_with_dalle(dalle_prompt)

            if image_url:
            
                st.image(image_url, caption=f"{st.session_state['selected_name']}")
                saved_image_path = save_image_from_url(image_url)
                # Store the image path in session state to access it in another tab
                st.session_state['saved_image_path'] = saved_image_path

                # Switch to the second tab to show the image
                st.rerun()

    with tab7:
        st.write("IMAGE TIMELINE")

        # Get and display the sorted images
        image_files = get_sorted_images()
        for image_file in image_files:
            st.image(image_file, width = 275, caption=os.path.basename(image_file))

    st.divider()
    st.button("RETURN TO MENU", key="return_main_from_chargen", on_click=update_return_to_main_menu)