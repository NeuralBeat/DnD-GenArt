import streamlit as st
from utils.specifc_callbacks import *

def ContinueJourneyInfo():
    spacer1, header_col, spacer2 = st.columns([1,2,1])
    with header_col:
        st.subheader("WELCOME TO HELL")
    
    st.divider()
    st.warning("SOON YOUR JOURNEY WILL CONTINUE HERE. THE DUNGEON MASTER IS STILL PREPARING ...")
    st.divider()
    st.button("RETURN TO MENU", key="return_main_from_chargen_2", on_click=update_return_to_main_menu)


def CharacterGeneratorInfo():
    st.write("CREATE NEW CHARACTER")

def RosterInfo():
    st.write("INSPECT YOUR ROSTER")