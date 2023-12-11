import streamlit as st
import os

# Step 1: Define Equipment Categories and Items
equipment = {
    "WEAPONS": ["SWORD", "BOW", "AXE", "STAFF"],
    "ARMOR": ["LEATHER ARMOR", "CHAIN MAIL", "PLATE ARMOR"],
    "HELMETS": ["IRON HELMET", "STEEL HELMET", "LEATHER HELMET"],
    "UTILITY": ["HEALING POTION", "ROPE", "TORCH", "MAP"]
    }

# Function to handle equipment selection
def handle_selection(category, items):
    selected_item = st.selectbox(f"SELECT {category}", [None] + items, key=f'select_{category}')
    if selected_item:
        st.session_state[f'selected_{category}'] = selected_item


# User Interface for Selections
def select_arsenal():
    st.title("SELECT YOUR ARSENAL")

    # Initialize or display current selections
    for category, items in equipment.items():
        if f'selected_{category}' not in st.session_state:
            st.session_state[f'selected_{category}'] = None
        handle_selection(category, items)

    if st.button("CONFIRM SELECTION"):
        show_selected_arsenal()
 

# Display Selected Equipment
def show_selected_arsenal():
    st.subheader("Your Selected Arsenal")
    for category in equipment.keys():
        if st.session_state[f'selected_{category}']:
            st.write(f"{category}: {st.session_state[f'selected_{category}']}")
