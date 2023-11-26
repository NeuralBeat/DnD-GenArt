import streamlit as st

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

    ##### INIT SESSION STATES ####
    if 'selected_class' not in st.session_state:
        st.session_state['selected_class'] = 'Select a class'

    if 'selected_subclass' not in st.session_state:
        st.session_state['selected_subclass'] = None

    #### SESSION INTERNAL CLASS SELECTION
    st.session_state['selected_class'] = st.selectbox(
    'Select your Class', 
    classes, 
    index=classes.index(default_class),
    key='class_selector'
    )

    # Update subclass state based on class selection
    if st.session_state['selected_class'] in subclasses:
        st.session_state['selected_subclass'] = st.selectbox(
            'Select your Subclass', 
            subclasses[st.session_state['selected_class']],
            index=0 if default_subclass not in subclasses[st.session_state['selected_class']] else subclasses[st.session_state['selected_class']].index(default_subclass),
            key='subclass_selector'
        )
    else:
        st.session_state['selected_subclass'] = ''