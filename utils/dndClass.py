import streamlit as st
import os

def select_class():
    default_class = st.session_state.get('selected_class', '')
    default_subclass = st.session_state.get('selected_subclass', '')

    classes = ['','Artificer', 'Barbarian', 'Bard', 'Blood Hunter', 'Cleric', 
               'Druid', 'Monk', 'Fighter', 'Paladin', 'Ranger', 
               'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

    subclasses = {
        'Artificer': ['Alchemist', 'Armorer', 'Artillerist', 'Battle Smith'],
        'Barbarian': ['Path of the Beast','Path of the Berserker', 'Path of the Totem Warrior', 'Path of the Ancestral Guardian', 'Path of the Storm Herald', 'Path of the Zealot'],
        'Bard': ['College of Creation', 'College of Glamour', 'College of Lore', 'College of Swords', 'College of Valor', 'College of Whispers', 'College of Eloquence'],
        'Blood Hunter': ['Order of the Ghostslayer', 'Order of the Lycan', 'Order of the Mutant', 'Order of the Profane Soul'],
        'Cleric': ['Order Domain', 'Forge Domain', 'Grave Domain', 'Knowledge Domain', 'Life Domain', 'Light Domain', 'Nature Domain', 'Peace Domain', 'Tempest Domain', 'Trickery Domain', 'Twilight Domain', 'War Domain'],
        'Druid': ['Circle of Dreams', 'Circle of Stars', 'Circle of Wildfire', 'Circle of the Land', 'Circle of the Moon', 'Circle of the Shepheard', 'Circle of Spores'],
        'Monk': ['Way of the Astral Self', 'Way of the Cobald Soul', 'Way of Mercy', 'Way of Shadow', 'Way of the Drunken Master', 'Way of the four Elements', 'Way of the Kensei', 'Way of the Open Hand', 'Way of the Sun Soul'],
        'Fighter': ['Arcane Archer', 'Battle Master', 'Cavalier', 'Champion', 'Eldritch Knight', 'Psi Warrior', 'Samurai'],
        'Paladin': ['Oath of Glory', 'Oath of Conquest', 'Oath of Devotion', 'Oath of Redemption', 'Oath of Vengeance', 'Oath of the Ancients', 'Oath of Watchers', 'Oath of the Open Sea'],
        'Ranger': ['Beast Master', 'Fey Wanderer', 'Gloomstalker', 'Horizonwalker', 'Hunter', 'Monster Slayer', 'Swarmkeeper'],
        'Rogue': ['Arcane Trickster', 'Assassin', 'Mastermind', 'Phantom', 'Scout', 'Swashbuckler', 'Soulknife', 'Thief'],
        'Sorcerer': ['Aberrant Mind', 'Clockwork Soul', 'Divine Soul', 'Draconic Bloodline', 'Shadow Magic', 'Storm Sorcery', 'Wild Magic'],
        'Warlock': ['Pact of the Archfey', 'Pact of the Celestial', 'Pact of the Fathomless', 'Pact of the Fiend', 'Pact of the Genie', 'Pact of the Great Old One', 'Pact of the Hexblade'],
        'Wizard': ['Bladesinger', 'Order of the Scribes', 'School of Abjuration', 'School of Conjuration', 'School of Divination', 'School of Enchantment', 'School of Evocation', 'School of Illusion', 'School of Necromancy', 'School of Transmutation', 'War Magic']
    }
    
    # Define the path to your images folder
    images_folder = 'images/classes'

    # Mapping of classes to their images
    class_images = {
        'Artificer': 'artificer.webp',
        'Barbarian': 'barbarian.webp',
        'Bard': 'bard.webp',
        'Blood Hunter': 'bloodhunter.webp',
        'Cleric': 'cleric.webp',
        'Druid': 'druid.webp',
        'Monk': 'monk.webp',
        'Fighter': 'fighter.webp',
        'Paladin': 'paladin.webp',
        'Ranger': 'ranger.webp',
        'Rogue': 'rogue.webp',
        'Sorcerer': 'sorcerer.webp',
        'Warlock': 'warlock.webp',
        'Wizard': 'wizard.webp'
    }

    ##### INIT SESSION STATES ####
    if 'selected_class' not in st.session_state:
        st.session_state['selected_class'] = 'Select a class'

    if 'selected_subclass' not in st.session_state:
        st.session_state['selected_subclass'] = None

    # Use columns to split the layout
    col1, col2 = st.columns(2)
    
    with col1:

        #### SESSION INTERNAL CLASS SELECTION
        st.session_state['selected_class'] = st.selectbox(
        'SELECT YOUR CLASS', 
        classes, 
        index=classes.index(default_class),
        key='class_selector',
        on_change=on_class_change
        )

        # Update subclass state based on class selection
        if st.session_state['selected_class'] in subclasses:
            st.session_state['selected_subclass'] = st.selectbox(
                'SELECT YOUR SUBCLASS', 
                subclasses[st.session_state['selected_class']],
                index=0 if default_subclass not in subclasses[st.session_state['selected_class']] else subclasses[st.session_state['selected_class']].index(default_subclass),
                key='subclass_selector',
                on_change=on_subclass_change
            )
        else:
            st.session_state['selected_subclass'] = ''
        
    with col2:
        # Create three columns for centering the image
        spacer1, image_col, spacer2 = st.columns([1, 2, 1])
        with image_col:
            # Display image based on selected class
            if st.session_state['selected_class'] in class_images:
                image_path = os.path.join(images_folder, class_images[st.session_state['selected_class']])
                st.image(image_path, caption=None, width=160)

def on_class_change():
    selected_class = st.session_state.class_selector
    st.session_state['selected_class'] = selected_class
    st.session_state['selected_subclass'] = None

def on_subclass_change():
    st.session_state['selected_subclass'] = st.session_state.subclass_selector