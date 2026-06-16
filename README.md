<<<<<<< HEAD
# LLM_Tokenization_logic
Learning AI Agent - tokenization, LLMs, and more

A hands-on learning journey building AI Agents from scratch using Python.

## Modules
- **01_Tokenization** - Understanding how LLMs tokenize text using tiktoken

## Setup
=======
A hands-on learning journey through AI/ML concepts — built from scratch using Python and the Gemini API.

## Modules

### 01_Tokenization
Understanding how LLMs tokenize text under the hood using `tiktoken`.

### hello_world
First experiments with the Gemini API:
- `gemini_hello.py` — Basic content generation using the native Gemini SDK
- `gemini_openai.py` — Using Gemini via the OpenAI-compatible client

### prompts
Exploring core prompting techniques:
- `zero_shot.py` — Asking the model directly with no examples
- `Few_shot.py` — Guiding the model with prior examples
- `cot.py` — Chain-of-thought: making the model think step by step before answering
- `persona_prompt.py` — Giving the model a specific identity/persona to respond as

## Setup

>>>>>>> 6c5d18f6aa4b55a6620070994164839c29960fec
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
<<<<<<< HEAD
```

## Tech Stack
- Python 3.14
- tiktoken
- More coming soon...
=======
Add your API key to a .env file:


GEMINI_API_KEY=YOUR_GEMINI_API_KEY
Tech Stack
Python 3.14
Google Gemini API
tiktoken
openai (OpenAI-compatible client for Gemini)
python-dotenv

>>>>>>> 6c5d18f6aa4b55a6620070994164839c29960fec
