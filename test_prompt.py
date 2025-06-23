from prompts import create_story_prompt

def test_prompt_includes_names_and_genre():
    names = ["Dayeon", "Tejas"]
    genre = "Horror"
    prompt = create_story_prompt(names, genre)

    assert "Dayeon" in prompt
    assert "Tejas" in prompt
    assert "horror" in prompt.lower()
