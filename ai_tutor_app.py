import streamlit as st
import os
from openai import OpenAI

# Load API key from Streamlit secrets
client = OpenAI(api_key=os.getenv("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"))

# Streamlit UI setup
st.set_page_config(page_title="AI Tutor", page_icon="🧠")
st.title("🧠 Your AI Tutor")
st.write("Ask any question related to AI and get a clear explanation.")

# Input field
user_input = st.text_input("What AI topic would you like to learn about? (e.g., 'distillation', 'transformers', 'RL')")

# When button is clicked
if st.button("Teach Me") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert AI tutor who explains technical concepts clearly and simply."},
                    {"role": "user", "content": user_input}
                ]
            )
            explanation = response.choices[0].message.content
            st.success("Here's your lesson:")
            st.markdown(explanation)
        except Exception as e:
            st.error(f"An error occurred: {e}")
