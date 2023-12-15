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
        'Bronze Dragon Ancestry': 'Dragonborn/CopperDragonAncestry.webp', 
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
        'Githzerai': 'Gith/Githzerai.webp',
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
        key='race_selector',
        on_change=on_race_change
        )
        st.session_state['selected_race'] = selected_race

        # Update subclass state based on class selection
        if selected_race in subraces:

            selected_subrace = st.selectbox(
                'SELECT YOUR SUBRACE OR ANCESTRY', 
                subraces[selected_race],
                index=0 if default_subrace not in subraces[selected_race] else subraces[selected_race].index(default_subrace),
                key='subrace_selector',
                on_change=on_subrace_change
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

def on_race_change():
    selected_race = st.session_state.race_selector
    st.session_state['selected_race'] = selected_race
    st.session_state['selected_subrace'] = None

def on_subrace_change():
    st.session_state['selected_subrace'] = st.session_state.subrace_selector

def apply_traits(selected_traits):
    for trait in selected_traits:
        st.session_state[trait] = True

def display_racial_traits():
    selected_subrace = st.session_state.get('selected_subrace', None)
    if selected_subrace and selected_subrace in subracial_traits:
        apply_traits(subracial_traits[selected_subrace])
        
        traits_list = subracial_traits[selected_subrace]
        traits_str = ', '.join(traits_list)
        st.caption(f":red[RACIAL TRAITS:] {traits_str}")


def display_background_traits():
    selected_background = st.session_state.get('selected_background', None)
    if selected_background and selected_background in background_proficiencies:
        apply_traits(background_proficiencies[selected_background])
        apply_traits(background_traits[selected_background])
        
        traits_list = background_traits[selected_background]
        traits_str = ', '.join(traits_list)
        prof_list = background_proficiencies[selected_background]
        prof_str = ', '.join(prof_list)
        st.caption(f":red[BACKGROUND TRAITS:] {traits_str}, :red[BACKGROUND PROFICIENCIES:] {prof_str}")

# Backgrounds and their associated skill proficiencies
backgrounds = {
    "": [""],
    "Acolyte": ["Insight", "Religion"],
    "Charlatan": ["Deception", "Sleight of Hand"],
    "Criminal/Spy": ["Deception", "Stealth"],
    "Entertainer": ["Acrobatics", "Performance"],
    "Folk Hero": ["Animal Handling", "Survival"],
    "Guild Artisan": ["Insight", "Persuasion"],
    "Hermit": ["Medicine", "Religion"],
    "Noble": ["History", "Persuasion"],
    "Outlander": ["Athletics", "Survival"],
    "Sage": ["Arcana", "History"],
    "Sailor": ["Athletics", "Perception"],
    "Soldier": ["Athletics", "Intimidation"],
    "Urchin": ["Sleight of Hand", "Stealth"]
}

def select_background():
    # Initialize the session state for selected background if it's not already set
    if 'selected_background' not in st.session_state:
        st.session_state['selected_background'] = None

    #default_background = st.session_state.get('selected_class', '')
    background_choices = list(backgrounds.keys())
    # Use the session state variable as the default value in the selectbox
    selected_background = st.selectbox(
        'SELECT YOUR BACKGROUND',
        options=background_choices,
        index=0 if st.session_state['selected_background'] is None else list(backgrounds.keys()).index(st.session_state['selected_background']),
        key='background_selector',
        on_change=on_background_change
    )

    # Update the session state based on the selection
    st.session_state['selected_background'] = selected_background

def on_background_change():
    st.session_state['selected_background'] = st.session_state.background_selector

background_traits = {
    "Acolyte": ["Shelter of the Faithful"],
    "Charlatan": ["False Identity"],
    "Criminal": ["Criminal Contact"],
    "Entertainer": ["By Popular Demand"],
    "Folk Hero": ["Rustic Hospitality"],
    "Guild Artisan": ["Guild Membership"],
    "Hermit": ["Discovery"],
    "Noble": ["Position of Privilege"],
    "Outlander": ["Wanderer"],
    "Sage": ["Researcher"],
    "Sailor": ["Ship's Passage"],
    "Soldier": ["Military Rank"],
    "Urchin": ["City Secrets"],
    "Haunted One": ["Heart of Darkness"],
    "Fisher": ["Fisher's Intuition"],
    "Gladiator": ["By Popular Demand (Gladiator Variant)"],
    "Knight": ["Retainers"],
    "Pirate": ["Bad Reputation"],
    "Mercenary Veteran": ["Mercenary Life"],
    "City Watch": ["Watcher's Eye"],
    "Clan Crafter": ["Respect of the Stout Folk"],
    "Cloistered Scholar": ["Library Access"],
    "Courtier": ["Court Functionary"],
    "Faction Agent": ["Safe Haven"],
    "Far Traveler": ["All Eyes on You"],
    "Inheritor": ["Inheritance"],
    "Knight of the Order": ["Knightly Regard"],
    "Urban Bounty Hunter": ["Ear to the Ground"]
}

background_proficiencies = {
    "Acolyte": ["INSIGHT", "RELIGION"],
    "Charlatan": ["DECEPTION", "SLEIGHT OF HAND"],
    "Criminal/Spy": ["DECEPTION", "STEALTH"],
    "Entertainer": ["ACROBATICS", "PERFORMANCE"],
    "Folk Hero": ["ANIMAL HANDLING", "SURVIVAL"],
    "Guild Artisan": ["INSIGHT", "PERSUASION"],
    "Hermit": ["MEDICINE", "RELIGION"],
    "Noble": ["HISTORY", "PERSUASION"],
    "Outlander": ["ATHLETICS", "SURVIVAL"],
    "Sage": ["ARCANA", "HISTORY"],
    "Sailor": ["ATHLETICS", "PERCEPTION"],
    "Soldier": ["ATHLETICS", "INTIMIDATION"],
    "Urchin": ["SLEIGHT OF HAND", "STEALTH"]
}

subracial_traits = {
    "Black Dragon Ancestry": ["Breath Weapon (Acid)", "Damage Resistance (Acid)"],
    "Blue Dragon Ancestry": ["Breath Weapon (Lightning)", "Damage Resistance (Lightning)"],
    "Brass Dragon Ancestry": ["Breath Weapon (Fire)", "Damage Resistance (Fire)"],
    "Bronze Dragon Ancestry": ["Breath Weapon (Lightning)", "Damage Resistance (Lightning)"],
    "Copper Dragon Ancestry": ["Breath Weapon (Acid)", "Damage Resistance (Acid)"],
    "Gold Dragon Ancestry": ["Breath Weapon (Fire)", "Damage Resistance (Fire)"],
    "Green Dragon Ancestry": ["Breath Weapon (Poison)", "Damage Resistance (Poison)"],
    "Red Dragon Ancestry": ["Breath Weapon (Fire)", "Damage Resistance (Fire)"],
    "Silver Dragon Ancestry": ["Breath Weapon (Cold)", "Damage Resistance (Cold)"],
    "White Dragon Ancestry": ["Breath Weapon (Cold)", "Damage Resistance (Cold)"],
    "Aasimar": ["Darkvision", "Celestial Resistance", "Healing Hands", "Light Bearer"],
    "Human": ["Extra Language"],
    "Air Genasi": ["Unending Breath", "Mingle with the Wind"],
    "Earth Genasi": ["Earth Walk", "Merge with Stone"],
    "Fire Genasi": ["Darkvision", "Damage Resistance (Fire)", "Reach to the Blaze"],
    "Water Genasi": ["Amphibious", "Swim", "Call to the Wave"],
    "Half-Orc": ["Darkvision", "Relentless Endurance", "Savage Attacks"],
    "Half-Elf": ["Darkvision", "Fey Ancestry", "Skill Versatility"],
    "Orc": ["Darkvision", "Aggressive", "Powerful Build", "Menacing"],
    "Bloodline of Asmodeus": ["Darkvision", "Hellish Resistance", "Infernal Legacy"],
    "Bloodline of Zariel": ["Darkvision", "Hellish Resistance", "Infernal Legacy"],
    "Bloodline of Mephistopheles": ["Darkvision", "Hellish Resistance", "Infernal Legacy"],
    "Lightfood Halfling": ["Lucky", "Brave", "Halfling Nimbleness"],
    "Stout Halfling": ["Lucky", "Brave", "Halfling Nimbleness"],
    "High Elf": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"],
    "Wood Elf": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"],
    "Eladrin Elf": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"],
    "Dark Elf": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"],
    "Hill Dwarf": ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning", "Tool Proficiency"],
    "Mountain Dwarf": ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning", "Tool Proficiency"],
    "Grey Dwarf": ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning", "Tool Proficiency"],
    "Forest Gnome": ["Darkvision", "Gnome Cunning"],
    "Rock Gnome": ["Darkvision", "Gnome Cunning"],
    "Deep Gnome": ["Darkvision", "Gnome Cunning"],
}