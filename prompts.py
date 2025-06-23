def create_story_prompt(names, genre):
    names_str = ", ".join(names)
    return f"""
Write a short and engaging {genre.lower()} story that features the following people as main characters: {names_str}.

Your story should include:
- A creative title
- A clear plot (can be funny, dramatic, scary or emotional)
- At least one memorable or unexpected moment
- An ending that surprises or wraps things up nicely

Keep it under 800 tokens.
"""