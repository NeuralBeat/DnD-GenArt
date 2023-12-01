import streamlit as st
import os
import glob
from utils.dndClass import *
from utils.dndRace import *
from utils.dndAlignment import *
from utils.dndCharacterLook import *
from utils.promptCreator import *


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

# Create tabs
tab1, tab2, tab3 = st.tabs(["CORE", "OPTICS", "EQUIPMENT"])

# Tab 1: Core Attributes (Class, Race, Alignment)
with tab1:
    # Call your function for selecting class, race, and alignment
    select_race()
    select_class()
    select_aligment()

# Tab 2: Optics (Character Look)
with tab2:
    select_character_look()

# Tab 3: Equipment
with tab3:
    pass

# Display the prompt
if st.button("Generate Character Prompt"):
    dalle_prompt = create_dalle_prompt()
    st.write("Generated Prompt for DALL-E:")
    st.markdown(f"> {dalle_prompt}")
    
    image_url = generate_image_with_dalle(dalle_prompt)
    if image_url:
        # Assuming the API returns the URL of the generated image
        st.image(image_url, caption="Generated Image")