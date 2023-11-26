import streamlit as st

def select_aligment():
    default_alignment = st.session_state.get('selected_alignment', '')

    alignments = ['','Lawful good','Neutral good', 'Chaotic good', 'Lawful neutral', 'True Neutral', 'Chaotic neutral', 'Lawful evil', 'Neutral evil', 'Chaotic evil']

        ##### INIT SESSION STATES ####
    if 'selected_alignment' not in st.session_state:
        st.session_state['selected_alignment'] = 'Select an alignment'

        #### SESSION INTERNAL CLASS SELECTION
    st.session_state['selected_alignment'] = st.selectbox(
    'Select your alignment', 
    alignments, 
    index=alignments.index(default_alignment),
    key='alignment_selector'
    )