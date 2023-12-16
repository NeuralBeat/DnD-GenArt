import streamlit as st
import os
from utils.attributeHandler import *

skills = {
    "ACROBATICS": "DEXTERITY",
    "ANIMAL HANDLING": "WISDOM",
    "ARCANA": "INTELLIGENCE",
    "ATHLETICS": "STRENGTH",
    "DECEPTION": "CHARISMA",
    "HISTORY": "INTELLIGENCE",
    "INSIGHT": "WISDOM",
    "INTIMIDATION": "CHARISMA",
    "INVESTIGATION": "INTELLIGENCE",
    "MEDICINE": "WISDOM",
    "NATURE": "INTELLIGENCE",
    "PERCEPTION": "WISDOM",
    "PERFORMANCE": "CHARISMA",
    "PERSUASION": "CHARISMA",
    "RELIGION": "INTELLIGENCE",
    "SLEIGHT OF HAND": "DEXTERITY",
    "STEALTH": "DEXTERITY",
    "SURVIVAL": "WISDOM"
}

class_skill_proficiencies = {
    "Artificer": ["ARCANA", "HISTORY", "INVESTIGATION", "MEDICINE", "NATURE", "PERCEPTION", "SLEIGHT OF HAND"],
    "Barbarian": ["ANIMAL HANDLING", "ATHLETICS", "INTIMIDATION", "NATURE", "PERCEPTION", "SURVIVAL"],
    "Bard": ["ACROBATICS", "ANIMAL HANDLING", "ARCANA", "ATHLETICS", "DECEPTION", "HISTORY", "INSIGHT", "INTIMIDATION", "INVESTIGATION", "MEDICINE", "NATURE", "PERCEPTION", "PERFORMANCE", "PERSUASION", "RELIGION", "SLEIGHT OF HAND", "STEALTH", "SURVIVAL"],
    "Blood Hunter": ["ACROBATICS", "ARCANA", "ATHLETICS", "HISTORY", "INSIGHT", "INVESTIGATION", "RELIGION", "SURVIVAL"],
    "Cleric": ["HISTORY", "INSIGHT", "MEDICINE", "PERSUASION", "RELIGION"],
    "Druid": ["ARCANA", "ANIMAL HANDLING", "INSIGHT", "MEDICINE", "NATURE", "PERCEPTION", "RELIGION", "SURVIVAL"],
    "Fighter": ["ACROBATICS", "ANIMAL HANDLING", "ATHLETICS", "HISTORY", "INSIGHT", "INTIMIDATION", "PERCEPTION", "SURVIVAL"],
    "Monk": ["ACROBATICS", "ATHLETICS", "HISTORY", "INSIGHT", "RELIGION", "STEALTH"],
    "Paladin": ["ATHLETICS", "INSIGHT", "INTIMIDATION", "MEDICINE", "PERSUASION", "RELIGION"],
    "Ranger": ["ANIMAL HANDLING", "ATHLETICS", "INSIGHT", "INVESTIGATION", "NATURE", "PERCEPTION", "STEALTH", "SURVIVAL"],
    "Rogue": ["ACROBATICS", "ATHLETICS", "DECEPTION", "INSIGHT", "INTIMIDATION", "INVESTIGATION", "PERCEPTION", "PERFORMANCE", "PERSUASION", "SLEIGHT OF HAND", "STEALTH"],
    "Sorcerer": ["ARCANA", "DECEPTION", "INSIGHT", "INTIMIDATION", "PERSUASION", "RELIGION"],
    "Warlock": ["ARCANA", "DECEPTION", "HISTORY", "INTIMIDATION", "INVESTIGATION", "NATURE", "RELIGION"],
    "Wizard": ["ARCANA", "HISTORY", "INSIGHT", "INVESTIGATION", "MEDICINE", "RELIGION"]
}

class_skill_choices = {
    "Artificer": 2,
    "Barbarian": 2,
    "Bard": 3,
    "Blood Hunter": 2,
    "Cleric": 2,
    "Druid": 2,
    "Fighter": 2,
    "Monk": 2,
    "Paladin": 2,
    "Ranger": 2,
    "Rogue": 3,
    "Sorcerer": 2,
    "Warlock": 2,
    "Wizard": 2,
}

background_skill_proficiencies = {
    "Acolyte": ["INSIGHT", "RELIGION"],
    "Charlatan": ["DECEPTION", "SLEIGHT OF HAND"],
    "Criminal": ["DECEPTION", "STEALTH"],
    "Entertainer": ["ACROBATICS", "PERFORMANCE"],
    "Folk Hero": ["ANIMAL HANDLING", "SURVIVAL"],
    "Guild Artisan": ["INSIGHT", "PERSUASION"],
    "Hermit": ["MEDICINE", "RELIGION"],
    "Noble": ["HISTORY", "PERSUASION"],
    "Outlander": ["ATHLETICS", "SURVIVAL"],
    "Sage": ["ARCANA", "HISTORY"],
    "Sailor": ["ATHLETICS", "PERCEPTION"],
    "Soldier": ["ATHLETICS", "INTIMIDATION"],
    "Urchin": ["SLEIGHT OF HAND", "STEALTH"],
    "Haunted One": ["ARCANA", "INGESTIGATION"],
    "Fisher": ["HISTORY", "SURVIVAL"],
    "Gladiator": ["ACROBATICS", "PERFORMANCE"],
    "Knight": ["HISTORY", "PERSUASION"],
    "Pirate": ["ATHLETICS", "PERCEPTION"],
    "Mercenary Veteran": ["ATHLETICS", "INTIMIDATION"],
    "City Watch": ["ATHLETICS", "INSIGHT"],
    "Clan Crafter": ["HISTORY", "INSIGHT"],
    "Cloistered Scholar": ["HISTORY", "RELIGION"],
    "Courtier": ["INSIGHT", "PERSUASION"],
    "Faction Agent": ["INSIGHT", "DECEPTION"],
    "Far Traveler": ["INSIGHT", "PERCEPTION"],
    "Inheritor": ["SURVIVAL", "ARCANA"],
    "Knight of the Order": ["PERSUASION", "HISTORY"],
    "Urban Bounty Hunter": ["PERSUASION", "STEALTH"]
}

background_languages = {
    "Acolyte": 2,
    "Charlatan": 1,
    "Criminal": 0,
    "Entertainer": 1,
    "Folk Hero": 1,
    "Guild Artisan": 1,
    "Hermit": 0,
    "Noble": 2,
    "Outlander": 1,
    "Sage": 2,
    "Sailor": 2,
    "Soldier": 1,
    "Urchin": 0,
    "Haunted One": 2,
    "Fisher": 0,
    "Gladiator": 2,
    "Knight": 1,
    "Pirate": 0,
    "Mercenary Veteran": 0,
    "City Watch": 2,
    "Clan Crafter": 1,
    "Cloistered Scholar": 2,
    "Courtier": 2,
    "Faction Agent": 2,
    "Far Traveler": 1,
    "Inheritor": 0,
    "Knight of the Order": 1,
    "Urban Bounty Hunter": 0
}

background_tool_proficiencies = {
    "Acolyte": [],
    "Charlatan": [],
    "Criminal": [],
    "Entertainer": [],
    "Folk Hero": [],
    "Guild Artisan": [],
    "Hermit": [],
    "Noble": [],
    "Outlander": [],
    "Sage": [],
    "Sailor": [],
    "Soldier": [],
    "Urchin": [],
    "Haunted One": [],
    "Fisher": [],
    "Gladiator": [],
    "Knight": [],
    "Pirate": [],
    "Mercenary Veteran": [],
    "City Watch": [],
    "Clan Crafter": [],
    "Cloistered Scholar": [],
    "Courtier": [],
    "Faction Agent": [],
    "Far Traveler": [],
    "Inheritor": [],
    "Knight of the Order": [],
    "Urban Bounty Hunter": []
}

def calculate_skill_modifier(skill, proficiency_bonus=0, proficient=False):
    ability = skills[skill]
    ability_modifier = calculate_modifier(st.session_state[ability])
    proficient = False

    selected_class = st.session_state.get('selected_class', None)
    try:
        num_skills = class_skill_choices[selected_class]
    
    except:
        num_skills = 0
    # Check if the skill is among the chosen class skills
    for i in range(num_skills): 
        session_state_key = f'class_skill_{i}'
        if st.session_state.get(session_state_key) == skill:
            proficient = True
            break
    
    # Check background skill proficiencies
    selected_background = st.session_state.get('selected_background', None)
    if selected_background and skill in background_skill_proficiencies.get(selected_background, []):
        proficient = True

    if proficient:
        return ability_modifier + proficiency_bonus
    else:
        return ability_modifier
    
    
def display_skills(proficiency_bonus=2):
    for skill, ability in skills.items():
        skill_modifier = calculate_skill_modifier(skill, proficiency_bonus)
        st.write(f"{skill} ({ability[:3]}): {skill_modifier:+d}")

def select_class_skills():
    # Check if a class is selected
    selected_class = st.session_state.get('selected_class', None)

    if selected_class and selected_class in class_skill_proficiencies:
        num_skills = class_skill_choices[selected_class]
        st.write(f"SELECT PROFICIENCIES - {selected_class}:")
        available_skills = class_skill_proficiencies[selected_class]

        # Reset previous skill choices when class changes
        for i in range(num_skills):
            st.session_state.pop(f'class_skill_{i}', None)

        # Create selectboxes for skill choices
        for i in range(num_skills):
            skill_key = f'class_skill_select_{i}'
            session_state_key = f'class_skill_{i}'

            # Create a selectbox and update the corresponding session state variable
            chosen_skill = st.selectbox(f"Skill {i+1}", [None] + available_skills, key=skill_key)
            if chosen_skill:
                st.session_state[session_state_key] = chosen_skill
        
        st.divider()

