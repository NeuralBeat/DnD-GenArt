from langchain.llms import OpenAI
from langchain.chains import SingleLM
import streamlit as st

# Set up OpenAI GPT
openai_api_key = "YOUR_OPENAI_API_KEY"
llm = OpenAI(api_key=openai_api_key)

# Create a LangChain chain with OpenAI GPT
chain = SingleLM(llm)

def DungeonMaster():
    st.title("AI Dungeon Master")

    if 'history' not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("Your action:")

    if st.button("Send"):
        st.session_state.history.append(f"You: {user_input}")
        response = chain.run_chain(st.session_state.history)
        st.session_state.history.append(f"AI Dungeon Master: {response}")
        
        for line in st.session_state.history[-10:]:
            st.write(line)