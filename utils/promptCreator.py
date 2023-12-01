import streamlit as st
import openai
import json

def create_dalle_prompt():
    # Extract the values from the session state
    sex = st.session_state.get('selected_sex', 'unknown')
    age = st.session_state.get('selected_age', 'unknown')
    physique = st.session_state.get('selected_physique', 'average')
    skin_color = st.session_state.get('selected_skin_color', 'unknown')
    scale_color = st.session_state.get('selected_scale_color', 'unknown')
    skin_taint = st.session_state.get('selected_skin_taint', 'none')
    hair_color = st.session_state.get('selected_hair_color', 'unknown')
    hair_length = st.session_state.get('selected_hair_length', 'unknown')
    hair_style = st.session_state.get('selected_hair_style', 'unknown')
    beard_style = st.session_state.get('selected_beard_style', 'none')
    tattoo_style = st.session_state.get('selected_tattoo_style', 'none')
    accessories = st.session_state.get('selected_accessories', 'none')
    race = st.session_state.get('selected_race', 'unknown')
    subrace = st.session_state.get('selected_subrace', 'unknown')
    classes = st.session_state.get('selected_class', 'unknown')
    subclass = st.session_state.get('selected_subclass', 'unknown')

    # Construct the prompt
    prompt = f"A character portrait of a {age}, {sex},"

    if race == 'Dragonborn':
        prompt += f" {race} {classes}, {subclass} with {scale_color} scales."
    
    elif race == 'Tiefling':
        prompt+= f' {race} {classes}, {subclass} with {skin_color} skin and {skin_taint} taint.'

    else:
        prompt += f" {subrace} {classes}, {subclass} with {skin_color} skin and {skin_taint} taint."

    prompt += f" {physique} build, "

    if hair_color != 'unknown':
        prompt += f" {hair_length} {hair_color} hair,"

    if hair_length != 'bald' and not 'unknown':
        prompt += f" styled in {hair_style},"

    if beard_style != 'none':
        prompt += f", and a {beard_style}."
    
    if tattoo_style != 'none':
        prompt += f"{tattoo_style} tattoos,"
    
    if accessories != 'none':
        prompt += f" wearing {accessories},"

    prompt += f" centered face portrait, avoid text, avoid watermarks, ultra realistic, dnd character art portrait, dark fantasy art, matte fantasy painting, deviantart artstation, by jason felix by steve argyle by tyler jacobson by peter mohrbacher by paul hedley, cinema."

    return prompt

def generate_image_with_dalle(prompt):
    
    # Load API key
    openai_api_key = load_api_key()

    # Set up the OpenAI client
    client = openai.OpenAI(api_key=openai_api_key)

    try:
        # Generate the image
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1792",
            quality="standard",
            n=1,
        )
        return response.data[0].url  # Return the URL of the generated image
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def load_api_key():
    with open('utils/secrets.json') as file:
        data = json.load(file)
        return data['openai_api_key']