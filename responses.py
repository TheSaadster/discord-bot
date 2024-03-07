import os
from random import choice, randint
from typing import Final
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_TOKEN: Final[str] = os.getenv("OPENAI_API_KEY")


client = OpenAI()


def get_response(user_input: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}]
    )
    return completion.choices[0].message.content
