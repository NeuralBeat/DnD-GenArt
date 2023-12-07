import streamlit as st
import os

def select_race():
    default_race = st.session_state.get('selected_race', '')
    default_subrace = st.session_state.get('selected_subrace', '')

    races = ['','Dragonborn','Dwarf','Elf','Genasi', 'Gith', 'Gnome', 'Halfling', 'Human', 'Orc','Tiefling']

    subraces = {
        'Dragonborn': ['Black Dragon Ancestry', 'Blue Dragon Ancestry', 'Brass Dragon Ancestry', 'Bronze Dragon Ancestry', 'Copper Dragon Ancestry', 'Gold Dragon Ancestry', 'Green Dragon Ancestry', 'Red Dragon Ancestry', 'Silver Dragon Ancestry', 'White Dragon Ancestry'],
        'Dwarf': ['Hill Dwarf', 'Mountain Dwarf', 'Grey Dwarf'],
        'Elf': ['Half-Elf','Dark Elf', 'Eladrin Elf', 'High Elf', 'Wood Elf'],
        'Genasi': ['Air Genasi', 'Earth Genasi', 'Fire Genasi', 'Water Genasi'],
        'Gith': ['Githyanki', 'Githzerai'],
        'Gnome': ['Rock Gnome', 'Forest Gnome', 'Deep Gnome'],
        'Halfling': ['Lightfoot Halfling', 'Stout Halfling'],
        'Human': ['Human', 'Aasimar'],
        'Orc': ['Half-Orc', 'Orc'],
        'Tiefling': ['Bloodline of Asmodeus', 'Bloodline of Mephistopheles', 'Bloodline of Zariel']
    }
        # Define the path to your images folder
    images_folder = 'images/races'

    # Mapping of races to their images
    subrace_images = {
        'Black Dragon Ancestry': 'Dragonborn/BlackDragonAncestry.webp', 
        'Blue Dragon Ancestry': 'Dragonborn/BlueDragonAncestry.webp', 
        'Brass Dragon Ancestry': 'Dragonborn/BrassDragonAncestry.webp', 
        'Bronze Dragon Ancestry': 'Dragonborn/BronzeDragonAncestry.webp', 
        'Copper Dragon Ancestry': 'Dragonborn/CopperDragonAncestry.webp', 
        'Gold Dragon Ancestry': 'Dragonborn/GoldDragonAncestry.webp', 
        'Green Dragon Ancestry': 'Dragonborn/GreenDragonAncestry.webp', 
        'Red Dragon Ancestry': 'Dragonborn/RedDragonAncestry.webp', 
        'Silver Dragon Ancestry': 'Dragonborn/SilverDragonAncestry.webp', 
        'White Dragon Ancestry': 'Dragonborn/WhiteDragonAncestry.webp',
        'Hill Dwarf': 'Dwarf/HillDwarf.webp',
        'Mountain Dwarf':'Dwarf/MountainDwarf.webp', 
        'Grey Dwarf':'Dwarf/GreyDwarf.webp',
        'Half-Elf':'Elf/HalfElves.webp',
        'Dark Elf':'Elf/DarkElves.webp', 
        'Eladrin Elf':'Elf/EladrinElves.webp', 
        'High Elf':'Elf/HighElves.webp', 
        'Wood Elf':'Elf/WoodElves.webp',
        'Air Genasi':'Genasi/AirGenasi.webp',
        'Earth Genasi':'Genasi/EarthGenasi.webp', 
        'Fire Genasi':'Genasi/FireGenasi.webp', 
        'Water Genasi':'Genasi/WaterGenasi.webp',
        'Githyanki': 'Gith/Githyanki.webp',
        'Githzerai': 'Gith/Githzrerai.webp',
        'Rock Gnome': 'Gnome/RockGnome.webp', 
        'Forest Gnome':'Gnome/ForestGnome.webp', 
        'Deep Gnome':'Gnome/DeepGnome.webp',
        'Lightfoot Halfling':'Halfling/LightfootHalfling.webp', 
        'Stout Halfling':'Halfling/StoutHalfling.webp',
        'Human':'Human/Human.webp',
        'Aasimar':'Human/Aasimar.webp',
        'Half-Orc':'Orc/HalfOrc.webp',
        'Orc':'Orc/Orc.webp',
        'Bloodline of Asmodeus': 'Tiefling/AsmodeusTiefling.webp', 
        'Bloodline of Mephistopheles':'Tiefling/MephistophelesTiefling.webp', 
        'Bloodline of Zariel': 'Tiefling/ZarielTiefling.webp'
    }

    ##### INIT SESSION STATES ####
    # Initialize session states for selected race and subrace
    if 'selected_race' not in st.session_state:
        st.session_state['selected_race'] = ''

    if 'selected_subrace' not in st.session_state:
        st.session_state['selected_subrace'] = ''
    

    # Use columns to split the layout
    col1, col2 = st.columns(2)

    with col1:
        #### SESSION INTERNAL CLASS SELECTION
        selected_race = st.selectbox(
        'SELECT YOUR RACE', 
        races, 
        index=races.index(default_race),
        key='race_selector'
        )
        st.session_state['selected_race'] = selected_race

        # Update subclass state based on class selection
        if selected_race in subraces:

            selected_subrace = st.selectbox(
                'SELECT YOUR SUBRACE OR ANCESTRY', 
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
            if selected_subrace in subrace_images:
                image_path = os.path.join(images_folder, subrace_images[selected_subrace])
                st.image(image_path, caption=None, width=160, output_format='PNG')
