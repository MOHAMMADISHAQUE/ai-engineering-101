from dotenv import load_dotenv
from openai import OpenAI
client = OpenAI()


load_dotenv()

response = client.responses.create(
    model="gpt-5.5",
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)
