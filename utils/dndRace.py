import streamlit as st
import os

def select_race():
    default_race = st.session_state.get('selected_race', '')
    default_subrace = st.session_state.get('selected_subrace', '')

    races = ['','Dragonborn','Dwarf','Elf','Genasi', 'Gnome', 'Halfling', 'Human', 'Orc','Tiefling']

    subraces = {
        'Dragonborn': ['Black Dragon Ancestry', 'Blue Dragon Ancestry', 'Brass Dragon Ancestry', 'Bronze Dragon Ancestry', 'Copper Dragon Ancestry', 'Gold Dragon Ancestry', 'Green Dragon Ancestry', 'Red Dragon Ancestry', 'Silver Dragon Ancestry', 'White Dragon Ancestry'],
        'Dwarf': ['Hill Dwarf', 'Mountain Dwarf', 'Grey Dwarf'],
        'Elf': ['Half-Elf','Dark Elf', 'Eladrin Elf', 'High Elf', 'Wood Elf'],
        'Genasi': ['Air Genasi', 'Earth Genasi', 'Fire Genasi', 'Water Genasi'],
        'Gnome': ['Rock Gnome', 'Forest Gnome', 'Deep Gnome'],
        'Halfling': ['Lightfoot Halfling', 'Stout Halfling'],
        'Human': ['Human', 'Aasimar'],
        'Orc': ['Half-Orc', 'Orc'],
        'Tiefling': ['Bloodline of Asmodeus', 'Bloodline of Mephistopheles', 'Bloodline of Zariel']
    }
        # Define the path to your images folder
    images_folder = 'images/races'

    # Mapping of races to their images
    race_images = {
        'Dragonborn': 'dragonborn.webp',
        'Dwarf': 'dwarf.webp',
        'Elf': 'elf.webp',
        'Genasi': 'genasi.webp',
        'Gnome': 'gnome.webp',
        'Halfling': 'halfling.webp',
        'Human': 'human.webp',
        'Orc': 'orc.webp',
        'Tiefling': 'tiefling.webp'
    }

    ##### INIT SESSION STATES ####
    # Initialize session states for selected race and subrace
    if 'selected_race' not in st.session_state:
        st.session_state['selected_race'] = ''

    if 'selected_subrace' not in st.session_state:
        st.session_state['selected_subrace'] = None
    

    # Use columns to split the layout
    col1, col2 = st.columns(2)

    with col1:
        #### SESSION INTERNAL CLASS SELECTION
        selected_race = st.selectbox(
        'Select your Race', 
        races, 
        index=races.index(default_race),
        key='race_selector'
        )
        st.session_state['selected_race'] = selected_race

        # Update subclass state based on class selection
        if selected_race in subraces:
            selected_subrace = st.selectbox(
                'Select your Subrace or Ancestry', 
                subraces[selected_race],
                index=0 if default_subrace not in subraces[selected_race] else subraces[selected_race].index(default_subrace),
                key='subrace_selector'
            )
        else:
            selected_subrace = ''
        st.session_state['selected_subrace'] = selected_subrace

    with col2:
        # Create three columns for centering the image
        spacer1, image_col, spacer2 = st.columns([1, 2, 1])
        with image_col:
            # Display image based on selected class
            if selected_race in race_images:
                image_path = os.path.join(images_folder, race_images[selected_race])
                st.image(image_path, caption=None, width=160, output_format='PNG')
