from skills import SKILLS

def extract_skills(text):
    """
    Extracts matching skills from the given text.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))