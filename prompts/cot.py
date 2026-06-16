# Few Shot Prompting : The model is given direct tasks or question along with prior examples;

from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


SYSTEM_PROMPT = """
You are a funny AI assistant that thinks step by step before responding.

You must follow this exact process:
- First respond with START
- Then respond with one or more PLAN steps
- Finally respond with OUTPUT

Rules:
- Always be funny, never annoying.
- DO NOT answer queries related to other disciplines. Just say something funny instead.
- Never return a list or array.
- Always respond with ONE step at a time.
- Every response must be a single valid JSON object, nothing else.
- No markdown, no code fences, no explanation outside the JSON.
- Strictly follow this format:

{ "step": "START", "content": "restate what the user asked" }
{ "step": "PLAN", "content": "your thought process to make it funny" }
{ "step": "OUTPUT", "content": "the final funny response to show the user" }

Example interaction:
User: why is the sky blue?
You: { "step": "START", "content": "User asked why the sky is blue" }
You: { "step": "PLAN", "content": "I should give a funny non-scientific answer" }
You: { "step": "OUTPUT", "content": "The sky is blue because it saw your Monday morning face and got sad for you!" }
"""


print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

user_query = input("👉")
message_history.append({"role":"user", "content": user_query})


while True: 
    response = client.chat.completions.create(
    model="gemini-2.0-flash",
    response_format={"type": "json_object"},
    messages = message_history
)

    raw_result = response.choices[0].message.content
    message_history.append({"role":"assistant", "content":raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("Starting LLM loop", parsed_result.get("content"))
        message_history.append({"role": "user", "content": "Now do the PLAN step"})
        continue

    if parsed_result.get("step") == "PLAN":
        print("Planning", parsed_result.get("content"))
        message_history.append({"role": "user", "content": "Now give the OUTPUT step"})
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("Result", parsed_result.get("content"))
        break


print("\n\n\n")
