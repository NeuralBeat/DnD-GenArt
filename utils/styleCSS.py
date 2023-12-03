import streamlit as st

def inject_css():
    st.markdown("""
        <style>
            /* Dark Fantasy Theme CSS */
        .css-18e3th9 {
                background-image: url('images/generic/diablo.jpeg');
                background-size: cover;
            }
                
        body {
                background-color: #121212; /* Dark background */
                color: #c0c0c0; /* Light grey text */
                font-family: 'Diablo', serif; /* Gothic-style font */
            }

        button {
                background-color: #3c2f2f; /* Dark red background */
                color: #ffffff; /* White text */
                border: 1px solid #4b3832; /* Dark border */
                border-radius: 5px; /* Slightly rounded corners */
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }

        button:hover {
            background-color: #4b3832; /* Slightly lighter red on hover */
        }
                
        </style>
        """, unsafe_allow_html=True)