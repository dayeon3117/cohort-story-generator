import os
import openai
from prompts import create_story_prompt
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_story(names, genre):
    prompt = create_story_prompt(names, genre)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"An error occurred while generating the story: {str(e)}"
