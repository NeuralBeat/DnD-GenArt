import streamlit as st
from main_menu import *
from utils.styleCSS import *
from utils.specifc_callbacks import *

from CharacterGenerator import *
from DungeonMaster import *
from Roster import *

inject_css()

def main():
    # Initialize the session state if it doesn't exist
    if 'selected_page' not in st.session_state:
        st.session_state['selected_page'] = None

    if st.session_state['selected_page'] == 'continue_journey':
        ContinueJourneyInfo()  # Render content for this page

    elif st.session_state['selected_page'] == 'character_generator':
        CharacterGenerator()  # Render content for this page

    elif st.session_state['selected_page'] == 'roster':
        Roster()  # Render content for this page

    else:
        st.title("QUILL & QUEST")
        st.subheader("YOUR DUNGEONS & DRAGONS 5E COMPANION")
        main_menu()


if __name__ == "__main__":
    main()
