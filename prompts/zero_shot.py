# Zero Shot Prompting 

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


SYSTEM_PROMPT = "You should only and only answer coding related question. DO NOT ANSWER ANYTHING ELSE. Your name is Jarvis. IF user asks anything else apart from coding just say sorry"


response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey! My name is Ishaque, tell a joke?"}
    ]
)

print(response.choices[0].message.content)
