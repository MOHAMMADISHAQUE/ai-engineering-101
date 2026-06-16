# Few Shot Prompting : The model is given direct tasks or question along with prior examples;

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


SYSTEM_PROMPT = """

You should only and only answer mathematics related question. DO NOT ANSWER ANYTHING ELSE. Your name is Jarvis. IF user asks anything else apart from coding just say sorry

Examples : 
Q: How to centre a div
A: Sorry! I can only help with Mathematics related questions

Q: Whats 2+2
A: It's 4

"""


response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey! My name is Ishaque, tell a joke?"}
    ]
)

print(response.choices[0].message.content)
