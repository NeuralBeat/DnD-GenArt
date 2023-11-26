import streamlit as st

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