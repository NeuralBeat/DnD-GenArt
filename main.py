import streamlit as st
import os
import glob
from utils.dndClass import *
from utils.dndRace import *
from utils.dndAlignment import *
from utils.dndCharacterLook import *
from utils.promptCreator import *
from utils.imageHandler import *
from utils.styleCSS import *

inject_css()

side_bar_img = "https://i.pinimg.com/564x/05/c1/5a/05c15aca14964af944aac1c638e1d7d2.jpg"

##### START WITH APP LAYOUT ######

#st.set_page_config(page_title="DnD Disguise", page_icon="https://i.pinimg.com/564x/05/c1/5a/05c15aca14964af944aac1c638e1d7d2.jpg")

########### NAVIGATIONBAR ###########

with st.sidebar:
    st.image(side_bar_img, use_column_width=True)
    st.title("D&D CHARACTER ART")
    st.info("This application automatically generates character portraits based on the selected attributes using AI.")

########## MAIN ###########

#st.title("D&D CHARACTER ART")
st.subheader("D&D CHARACTER GENERATOR", anchor=None)

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["CORE", "OPTICS", "ARSENAL", "PORTRAIT"])

# Tab 1: Core Attributes (Class, Race, Alignment)
with tab1:
    # Call your function for selecting class, race, and alignment
    select_race()
    select_class()
    #select_aligment()

# Tab 2: Optics (Character Look)
with tab2:
    select_character_look()

# Tab 3: Equipment & Arsenal
with tab3:
    pass

with tab4:
    st.write("IMAGE TIMELINE")

    # Get and display the sorted images
    image_files = get_sorted_images()
    for image_file in image_files:
        st.image(image_file, width = 275, caption=os.path.basename(image_file))

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