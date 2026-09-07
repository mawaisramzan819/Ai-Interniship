"""
Task 1: OpenAI API Setup & Basic Calls
- Secure API key loading using python-dotenv
- Basic chat completion
- Inspect prompt, completion, and total token usage
- Basic temperature testing (0.0, 0.7, 1.5)
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load environment variables
load_dotenv()

# 2. Initialize Client (Supports Groq free endpoint or direct OpenAI)
api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
base_url = "https://api.groq.com/openai/v1" if os.getenv("GROQ_API_KEY") else None

if not api_key:
    raise ValueError("Missing API key! Please set GROQ_API_KEY or OPENAI_API_KEY in your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

# Select default model based on provider
model_name = "openai/gpt-oss-120b" if base_url else "gpt-4o-mini"

print(f"Connected to provider using model: {model_name}\n")

# 3. First Simple Completion
prompt = "What are the three most important responsibilities of an AI Engineer? Answer in 3 bullet points."

print("=" * 60)
print("1. Standard Completion & Token Usage Inspection")
print("=" * 60)

response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are an expert AI Engineering career advisor."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=200
)

print("\nPrompt:", prompt)
print("\nResponse:")
print(response.choices[0].message.content)

print("\n--- Token Usage Breakdown ---")
print(f"Prompt Tokens:     {response.usage.prompt_tokens}")
print(f"Completion Tokens: {response.usage.completion_tokens}")
print(f"Total Tokens:      {response.usage.total_tokens}")

# 4. Experimenting with Temperature: 0.0 vs 0.7 vs 1.5
print("\n" + "=" * 60)
print("2. Temperature Comparison Experiment")
print("=" * 60)

temp_prompt = "Write a one-sentence marketing tagline for a robotic coffee maker."
temperatures = [0.0, 0.7, 1.5]

for temp in temperatures:
    print(f"\n[Testing Temperature = {temp}]")
    res = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": temp_prompt}],
        temperature=temp,
        max_tokens=60
    )
    print("Tagline:", res.choices[0].message.content.strip())
