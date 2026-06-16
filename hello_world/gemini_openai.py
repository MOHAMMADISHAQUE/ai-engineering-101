from dotenv import load_dotenv
from openai import OpenAI
client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


load_dotenv()

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages = [
        {"role": "system", "content": "You're an expert comedian who only cracks joke"},
        {"role": "user", "content": "Hey! My name is Ishaque, who are you?"}
    ]
)

print(response.choices[0].message.content)
