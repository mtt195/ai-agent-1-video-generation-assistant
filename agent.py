# implements the core logic responsible for communicating with language model

from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

load_dotenv()
client = OpenAI()

def generate_prompts(scene_description: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": scene_description}
        ],
    )
    return response.choices[0].message.content