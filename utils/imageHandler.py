import requests
import streamlit as st
from PIL import Image
from io import BytesIO
import os

def save_image_from_url(image_url, folder='history/Portraits'):
    try:
        # Determine the filename
        filename = st.session_state.get('selected_name', 'character_portrait')

        # Create the folder if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Fetch the image from the URL
        response = requests.get(image_url)
        response.raise_for_status()  # Raises HTTPError if the HTTP request returned an unsuccessful status code

        # Convert the image content to a Pillow Image object
        image = Image.open(BytesIO(response.content))

        # Save the image in .webp format
        image_path = os.path.join(folder, f"{filename}.webp")
        image.save(image_path, 'WEBP')

        return image_path
    
    except Exception as e:
        print(f"An error occurred while saving the image: {e}")
        return None

def get_sorted_images(folder='history/Portraits'):
    # Get all files in the folder
    files = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith('.webp')]
    # Sort files by modification time, newest first
    files.sort(key=os.path.getmtime, reverse=True)
    return files