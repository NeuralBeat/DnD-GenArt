import base64
import os
import streamlit as st
from st_clickable_images import clickable_images

def get_absolute_path(relative_path):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, relative_path)

def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded_string}"

def main_menu():
    left_img_path = get_absolute_path("images/generic/DnDCompass.webp")
    center_img_path = get_absolute_path("images/generic/DnDMask.webp")
    right_img_path = get_absolute_path("images/generic/DnDRoster.webp")

    left_img_base64 = get_image_as_base64(left_img_path)
    center_img_base64 = get_image_as_base64(center_img_path)
    right_img_base64 = get_image_as_base64(right_img_path)

    # URLs of your images
    image_urls = [
        left_img_base64,  # Replace with your actual image path or URL
        center_img_base64,
        right_img_base64
    ]

    # Titles for your images
    titles = ["CONTINUE ADVENTURE", "CREATE NEW CHARACTER", "YOUR HERO ROSTER"]

    # Display clickable images
    selected_main_image = clickable_images(
        paths=image_urls,
        titles=titles,
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"}
    )

    if selected_main_image != -1 and not st.session_state.get('image_processed', False):
       st.session_state['selected_page'] = ['continue_journey', 'character_generator', 'roster'][selected_main_image]
       st.rerun()