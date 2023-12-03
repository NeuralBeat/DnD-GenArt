import streamlit as st

def inject_css():
    st.markdown("""
        <style>
            /* Dark Fantasy Theme CSS */

        @font-face {
                font-family: 'Diablo';
                src: url('https://raw.githubusercontent.com/yourusername/your-repo/main/fonts/Diablo.ttf') format('truetype');
                font-weight: normal;
                font-style: normal;
            }
        
        html, body, h1, h2, h3, h4, h5, h6, p, div, span, input, select, button {
                font-family: 'Diablo', sans-serif;
            }
                
        body {
                background-image: url('./images/generic/cathedral.png');
                background-size: cover; /* Cover the entire page */
                background-repeat: no-repeat; /* Do not repeat the image */
                background-attachment: fixed; /* Fixed background */
                background-position: center; /* Center the background image */
                font-family: 'Diablo', sans-serif;
            }

        button {
                font-family: 'Diablo', sans-serif;
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