import streamlit as st


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

    st.write(f"OPEN POINTS: {st.session_state['available_points']}")

    select_attribute_bonus()

    for attr in attributes:
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        with col1:
            st.write(f"{attr}")
        with col2:
            st.button("-", key=f"minus_{attr}", on_click=decrement_attribute, args=(attr,))
        with col3:
            st.write(f"{st.session_state[attr]}")
        with col4:
            st.button("+", key=f"plus_{attr}", on_click=increment_attribute, args=(attr,))

    st.info(f"MOST IMPORTANT STATS FOR {st.session_state['selected_class']} CLASS:")

def select_attribute_bonus():
    # Option selection
    bonus_option = st.radio("CHOOSE YOU ATTRIBUTE BONUS",
                            ("+2/+1", "+1/+1/+1"),
                            key="racial_bonus_option")

    # Initialize session state for bonus choices
    if 'bonus_choice_1' not in st.session_state:
        st.session_state['bonus_choice_1'] = 'STRENGTH'
    if 'bonus_choice_2' not in st.session_state:
        st.session_state['bonus_choice_2'] = 'DEXTERITY'
    if 'bonus_choice_3' not in st.session_state:
        st.session_state['bonus_choice_3'] = 'CONSTITUTION'

    attributes = ['STRENGTH', 'DEXTERITY', 'CONSTITUTION', 'INTELLIGENCE', 'WISDOM', 'CHARISMA']

    if bonus_option == "+2/+1":
        st.session_state['bonus_choice_1'] = st.selectbox("CHOOSE ATTRIBUTE FOR +2 BONUS", attributes, key='bonus_1')
        st.session_state['bonus_choice_2'] = st.selectbox("CHOOSE ATTRIBUTE FOR +1 BONUS", attributes, key='bonus_2')

        # Apply bonuses
        for attr in attributes:
            st.session_state[attr] = 8  # Reset to base value
        st.session_state[st.session_state['bonus_choice_1']] += 2
        st.session_state[st.session_state['bonus_choice_2']] += 1

    elif bonus_option == "+1/+1/+1":
        st.session_state['bonus_choice_1'] = st.selectbox("FIRST ATTRIBUTE FOR +1 BONUS", attributes, key='bonus_3')
        st.session_state['bonus_choice_2'] = st.selectbox("SECOND ATTRIBUTE FOR +1 BONUS", attributes, key='bonus_4')
        st.session_state['bonus_choice_3'] = st.selectbox("THIRD ATTRIBUTE FOR +1 BONUS", attributes, key='bonus_5')

        # Apply bonuses
        for attr in attributes:
            st.session_state[attr] = 8  # Reset to base value
        st.session_state[st.session_state['bonus_choice_1']] += 1
        st.session_state[st.session_state['bonus_choice_2']] += 1
        st.session_state[st.session_state['bonus_choice_3']] += 1