from openai import OpenAI

from config import OPENAI_API_KEY
from prompts import SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_resume(resume_text, jd_text):

    prompt = f"""
Resume

{resume_text}

----------------------------------------

Job Description

{jd_text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content