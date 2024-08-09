from dotenv import load_dotenv
import os
import json

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "can you JUST give the answer? Do not say anything else. Just write what you would type if you had to code in python and do not have ```python``` .",
        },
        {
            "role": "user",
            "content": "can you write me a pythong code for saying HEllo this is my first time running a code through llm and print",
        },
    ],
)
run = response.choices[0].message.content
exec(run)

# def save_gpt_output(output):
#     with open("output.txt", "w") as f:
#         json.dump(output, f)


# def read_gpt_output():
#     with open("output.txt", "r") as f:
#         return json.load(f)
