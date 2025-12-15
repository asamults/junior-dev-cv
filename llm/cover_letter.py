import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

with open("data/resume.txt") as f:
    RESUME = f.read()


def generate_cover_letter(job):
    prompt = f"""
Write a concise UK-style cover letter (100–120 words)
for a Junior Python Developer or Junior Data Engineer role.

Job description:
{job.get('description', '')}

Candidate CV:
{RESUME}

Tone: professional, motivated, junior-level
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful career assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.6,
    )

    return response.choices[0].message["content"]
