import streamlit as st
import json
from utils.generate_story import get_story

st.set_page_config(page_title="Cohort Story Generator", layout="centered")
st.title("Cohort Story Generator")
st.markdown("Select some friends and a genre, then let the AI write a story for you. It’s just for fun!")

# Load names
with open("cohort_list.json") as f:
    cohort_names = json.load(f)

# Genre picker
genre = st.selectbox("Choose a story theme:", [
    "Drama", "Romance", "Action", "Thriller", "Comedy", "Horror", "Crime", "Fantasy", "Sci-Fi", "Mystery"
])

# Name picker
selected_names = st.multiselect("Choose your characters:", cohort_names)

# Button click
if st.button("Generate Story"):
    if len(selected_names) < 2:
        st.warning("Please pick at least 2 people.")
    else:
        with st.spinner("Writing your story..."):
            story = get_story(selected_names, genre)
            if story.startswith("An error occurred"):
                st.error(story)
            else:
                st.markdown("## Your Story")
                st.write(story)