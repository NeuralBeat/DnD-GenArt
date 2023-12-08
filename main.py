import os
import base64
from utils.styleCSS import *
from streamlit_image_select import image_select
from st_clickable_images import clickable_images
from CharacterGenerator import *
from DungeonMaster import *

inject_css()


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

    # Handle actions based on clicked image
    if selected_main_image == 0:
        st.session_state['selected_page'] = 'continue_journey'
    elif selected_main_image == 1:
        st.session_state['selected_page'] = 'character_generator'
    elif selected_main_image == 2:
        st.session_state['selected_page'] = 'roster'


def get_absolute_path(relative_path):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, relative_path)

def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded_string}"

def main():
    # Initialize the session state if it doesn't exist
    if 'selected_page' not in st.session_state:
        st.session_state['selected_page'] = None

    if st.session_state['selected_page'] == 'continue_journey':
        ContinueJourneyInfo()  # Render content for this page
    elif st.session_state['selected_page'] == 'character_generator':
        CharacterGenerator()  # Render content for this page
    elif st.session_state['selected_page'] == 'roster':
        RosterInfo()  # Render content for this page
    else:
        st.title("QUILL & QUEST")
        st.subheader("YOUR DUNGEONS & DRAGONS 5E COMPANION")
        main_menu()

if __name__ == "__main__":
    main()
