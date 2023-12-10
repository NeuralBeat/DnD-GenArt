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
    
    if 'apply_bonus' not in st.session_state:
        st.session_state['apply_bonus'] = True  # Flag to control bonus application

    # Initialize attribute values in the session state
    for attr in attributes:
        if attr not in st.session_state:
            st.session_state[attr] = 8  # Default starting value
    
    st.write(f"OPEN POINTS: {st.session_state['available_points']}")

    select_attribute_bonus()

    for attr in attributes:
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        
        with col1:
            st.write(f"{attr}")
        
        with col2:
            st.button("DECREASE", key=f"minus_{attr}", on_click=decrement_attribute, args=(attr,))

        with col3:
            st.write(f"{st.session_state[attr]}")

        with col4:
            st.button("INCREASE", key=f"plus_{attr}", on_click=increment_attribute, args=(attr,))

    if st.session_state['selected_class'] in class_primary_attributes:
        primary_attrs = class_primary_attributes[st.session_state['selected_class']]
        st.info(f"PRIMARY STATS FOR {st.session_state['selected_class']}: {', '.join(primary_attrs)}")

def select_attribute_bonus():
    bonus_option = st.radio("CHOOSE ATTRIBUTE BONUS",
                            ("+2/+1", "+1/+1/+1"), horizontal=True,
                            key="racial_bonus_option")

    attributes = ['STRENGTH', 'DEXTERITY', 'CONSTITUTION', 'INTELLIGENCE', 'WISDOM', 'CHARISMA']

    display_bonus_selection(attributes, bonus_option)

    # Apply bonuses if they haven't been applied yet or if the option has changed
    if 'bonuses_applied' not in st.session_state or not st.session_state['bonuses_applied'] or st.session_state['previous_bonus_option'] != bonus_option:
        apply_racial_bonus(attributes, bonus_option)
        st.session_state['previous_bonus_option'] = bonus_option

def reset_attributes_to_base(attributes):
    for attr in attributes:
        st.session_state[attr] = 8  # Reset to base value

def display_bonus_selection(attributes, bonus_option):
    if bonus_option == "+2/+1":
        st.session_state['bonus_choice_1'] = st.selectbox("CHOOSE ATTRIBUTE FOR +2 BONUS", attributes, key='bonus_1')
        st.session_state['bonus_choice_2'] = st.selectbox("CHOOSE ATTRIBUTE FOR +1 BONUS", attributes, key='bonus_2')
    elif bonus_option == "+1/+1/+1":
        st.session_state['bonus_choice_1'] = st.selectbox("FIRST ATTRIBUTE FOR +1 BONUS", attributes, key='bonus_3')
        st.session_state['bonus_choice_2'] = st.selectbox("SECOND ATTRIBUTE FOR +1 BONUS", attributes, key='bonus_4')
        st.session_state['bonus_choice_3'] = st.selectbox("THIRD ATTRIBUTE FOR +1 BONUS", attributes, key='bonus_5')

def apply_racial_bonus(attributes, bonus_option):
    # Reset attributes to base value
    #reset_attributes_to_base(attributes)
    # Apply the bonuses
    if bonus_option == "+2/+1":
        st.session_state[st.session_state['bonus_choice_1']] += 2
        st.session_state[st.session_state['bonus_choice_2']] += 1
    elif bonus_option == "+1/+1/+1":
        st.session_state[st.session_state['bonus_choice_1']] += 1
        st.session_state[st.session_state['bonus_choice_2']] += 1
        st.session_state[st.session_state['bonus_choice_3']] += 1
    
    # Update the flag to indicate bonuses have been applied
    st.session_state['bonuses_applied'] = True