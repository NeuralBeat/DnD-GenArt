import streamlit as st

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

        ##### INIT SESSION STATES ####
    if 'selected_race' not in st.session_state:
        st.session_state['selected_race'] = 'Select a race'

    if 'selected_subrace' not in st.session_state:
        st.session_state['selected_subrace'] = None

        #### SESSION INTERNAL CLASS SELECTION
    st.session_state['selected_race'] = st.selectbox(
    'Select your Race', 
    races, 
    index=races.index(default_race),
    key='race_selector'
    )

    # Update subclass state based on class selection
    if st.session_state['selected_race'] in subraces:
        st.session_state['selected_subrace'] = st.selectbox(
            'Select your Subrace or Ancestry', 
            subraces[st.session_state['selected_race']],
            index=0 if default_subrace not in subraces[st.session_state['selected_race']] else subraces[st.session_state['selected_race']].index(default_subrace),
            key='subrace_selector'
        )
    else:
        st.session_state['selected_subrace'] = ''
