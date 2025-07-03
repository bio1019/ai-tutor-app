import streamlit as st
import openai
import os

# Load your API key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

# App title
st.set_page_config(page_title="AI Tutor", page_icon="🧠")
st.title("🧠 Your AI Tutor")
st.write("Ask a question about any AI topic and get a clear explanation.")

# Input from user
user_input = st.text_input("What AI topic would you like to learn about? (e.g., 'distillation', 'transformers', 'RL')")

# Button to submit
if st.button("Teach Me") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert AI tutor who explains concepts clearly and simply."},
                    {"role": "user", "content": user_input}
                ]
            )
            explanation = response["choices"][0]["message"]["content"]
            st.success("Here's what I found:")
            st.markdown(explanation)
        except Exception as e:
            st.error(f"Error: {e}")

