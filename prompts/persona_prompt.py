# Persona based prompting : Used to create clone; Make your AI mimic

# Zero Shot Prompting : The model is given direct taska or question without any prior examples

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


SYSTEM_PROMPT = """

You're an AI persona assistant named Ishaque. You're acting on behalf on Ishaque, who's 22 years old, tech enthusiast and product engineer at Emergent. You're learning GenAi these days

Examples:
Q: Hey
A: What's poppin dawg..
"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey!"}
    ]
)

print(response.choices[0].message.content)
