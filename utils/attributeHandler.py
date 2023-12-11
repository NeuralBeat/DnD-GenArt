import streamlit as st
from utils.dndClass import *

class_primary_attributes = {
    'Artificer': ['INTELLIGENCE', 'CONSTITUTION'],
    'Barbarian': ['STRENGTH', 'CONSTITUTION'],
    'Bard': ['CHARISMA', 'DEXTERITY'],
    'Blood Hunter': ['DEXTERITY', 'INTELLIGENCE'],
    'Cleric': ['WISDOM', 'CONSTITUTION'],
    'Druid': ['WISDOM', 'INTELLIGENCE'],
    'Fighter': ['STRENGTH', 'CONSTITUTION'],
    'Monk': ['DEXTERITY', 'WISDOM'],
    'Paladin': ['STRENGTH', 'CHARISMA'],
    'Ranger': ['DEXTERITY', 'WISDOM'],
    'Rogue': ['DEXTERITY', 'INTELLIGENCE'],
    'Sorcerer': ['CHARISMA', 'CONSTITUTION'],
    'Warlock': ['CHARISMA', 'CONSTITUTION'],
    'Wizard': ['INTELLIGENCE', 'CONSTITUTION']
}

def increment_attribute(attr_name):
    point_cost = 2 if st.session_state[attr_name] >= 15 else 1
    if st.session_state[attr_name] <= 15 and st.session_state['available_points'] >= point_cost:
        st.session_state[attr_name] += 1
        st.session_state['available_points'] -= point_cost

def decrement_attribute(attr_name):
    point_gain = 2 if st.session_state[attr_name] > 15 else 1
    if st.session_state[attr_name] > 6:
        st.session_state[attr_name] -= 1
        st.session_state['available_points'] += point_gain       

def select_attributes():
    
    attributes = ['STRENGTH', 'DEXTERITY', 'CONSTITUTION', 'INTELLIGENCE', 'WISDOM', 'CHARISMA']

    # Initialize available points
    total_points = 27
    if 'available_points' not in st.session_state:
        st.session_state['available_points'] = total_points

    # Initialize attribute values in the session state
    for attr in attributes:
        if attr not in st.session_state:
            st.session_state[attr] = 8  # Default starting value
    
    st.markdown(f":red[**OPEN** **POINTS**: **{st.session_state['available_points']}**]")

    select_attribute_bonus()
    apply_racial_bonus()
    st.divider()
    for attr in attributes:
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        
        with col1:
            st.write(f"{attr}")
        
        with col2:
            st.button("DECREASE", key=f"minus_{attr}", on_click=decrement_attribute, args=(attr,))

        with col3:
            if st.session_state[attr] >= 16:
                st.markdown(f":green[{st.session_state[attr]}]")
            if 10 <= st.session_state[attr] <=15:
                st.markdown(f":yellow[{st.session_state[attr]}]")
            if st.session_state[attr] <= 9:
                st.markdown(f":red[{st.session_state[attr]}]")

        with col4:
            st.button("INCREASE", key=f"plus_{attr}", on_click=increment_attribute, args=(attr,))

    st.divider()

    if st.session_state['selected_class'] in class_primary_attributes:
        primary_attrs = class_primary_attributes[st.session_state['selected_class']]
        st.info(f"PRIMARY STATS FOR {st.session_state['selected_class']}: {', '.join(primary_attrs)}")

def select_attribute_bonus():
    bonus_option = st.radio("CHOOSE YOUR ATTRIBUTE BONUS",
                            ("+2/+1", "+1/+1/+1"), horizontal=True,
                            key="racial_bonus_option")

    attributes = ['STRENGTH', 'DEXTERITY', 'CONSTITUTION', 'INTELLIGENCE', 'WISDOM', 'CHARISMA']
    
    # Set default values for bonus choices if not already set
    if 'bonus_choice_1' not in st.session_state:
        st.session_state['bonus_choice_1'] = 'DEXTERITY'
    if 'bonus_choice_2' not in st.session_state:
        st.session_state['bonus_choice_2'] = 'CONSTITUTION'
    if 'bonus_choice_3' not in st.session_state:
        st.session_state['bonus_choice_3'] = 'WISDOM'


    if bonus_option == "+2/+1":
        col1, col2 = st.columns(2)
        with col1:
            st.session_state['bonus_choice_1'] = st.selectbox("ATTRIBUTE FOR +2 BONUS", attributes, index=attributes.index(st.session_state['bonus_choice_1']), key='bonus_1')
        with col2:
            st.session_state['bonus_choice_2'] = st.selectbox("ATTRIBUTE FOR +1 BONUS", attributes, index=attributes.index(st.session_state['bonus_choice_2']), key='bonus_2')
    
    elif bonus_option == "+1/+1/+1":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.session_state['bonus_choice_1'] = st.selectbox("FIRST ATTRIBUTE +1", attributes, index=attributes.index(st.session_state['bonus_choice_1']), key='bonus_3')
        with col2:
            st.session_state['bonus_choice_2'] = st.selectbox("SECOND ATTRIBUTE +1", attributes, index=attributes.index(st.session_state['bonus_choice_2']), key='bonus_4')
        with col3:
            st.session_state['bonus_choice_3'] = st.selectbox("THIRD ATTRIBUTE +1", attributes, index=attributes.index(st.session_state['bonus_choice_3']), key='bonus_5')

def apply_racial_bonus():
    bonus_option = st.session_state['racial_bonus_option']
    attributes = ['STRENGTH', 'DEXTERITY', 'CONSTITUTION', 'INTELLIGENCE', 'WISDOM', 'CHARISMA']
    
    # Reset all bonuses before applying new ones
    for attr in attributes:
        st.session_state[attr] -= st.session_state.get(f'bonus_{attr}', 0)
        st.session_state[f'bonus_{attr}'] = 0

    # Apply new bonuses
    if bonus_option == "+2/+1":
        st.session_state[f'bonus_{st.session_state["bonus_choice_1"]}'] = 2
        st.session_state[f'bonus_{st.session_state["bonus_choice_2"]}'] = 1
    elif bonus_option == "+1/+1/+1":
        st.session_state[f'bonus_{st.session_state["bonus_choice_1"]}'] = 1
        st.session_state[f'bonus_{st.session_state["bonus_choice_2"]}'] = 1
        st.session_state[f'bonus_{st.session_state["bonus_choice_3"]}'] = 1

    for attr in attributes:
        st.session_state[attr] += st.session_state[f'bonus_{attr}']


def reset_previous_bonus(attributes):
    """Resets the previously applied racial bonuses."""
    for attr in attributes:
        if st.session_state.get(f'prev_bonus_{attr}'):
            st.session_state[attr] -= st.session_state[f'prev_bonus_{attr}']
            st.session_state[f'prev_bonus_{attr}'] = 0