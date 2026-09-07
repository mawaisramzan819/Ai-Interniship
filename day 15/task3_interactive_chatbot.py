"""
Task 3: Interactive CLI Chatbot with Conversation Context & Cost Tracking
- Persistent multi-turn conversation history
- System role persona definition
- Error handling for rate limits and API failures
- Token usage tracking and cost calculation
- Special commands: 'exit'/'quit' to finish, '/clear' to reset memory
"""

import os
from dotenv import load_dotenv
from openai import OpenAI, APIError, RateLimitError

# 1. Environment & Setup
load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
base_url = "https://api.groq.com/openai/v1" if os.getenv("GROQ_API_KEY") else None

client = OpenAI(api_key=api_key, base_url=base_url)
model_name = "openai/gpt-oss-120b" if base_url else "gpt-4o-mini"

# Pricing rates per 1M tokens ($)
PRICE_PER_1M_PROMPT = 0.15
PRICE_PER_1M_COMPLETION = 0.60

# 2. Conversation Memory & Token Counters
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a concise, friendly AI Engineering mentor named Ada. Explain concepts clearly and concisely."
}

messages = [SYSTEM_PROMPT.copy()]
total_prompt_tokens = 0
total_comp_tokens = 0

print("=" * 65)
print("🤖 Interactive AI Chatbot (Ada)")
print("Commands: 'exit'/'quit' to end | '/clear' to reset memory")
print("=" * 65 + "\n")

# 3. Interactive Loop
while True:
    try:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("\nSession ended by user.")
            break

        if user_input.lower() == "/clear":
            messages = [SYSTEM_PROMPT.copy()]
            print("\n🔄 Conversation memory cleared!\n")
            continue

        # Add user message to conversation history
        messages.append({"role": "user", "content": user_input})

        # Make API request with full historical context
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.7
        )

        reply = response.choices[0].message.content
        p_tokens = response.usage.prompt_tokens
        c_tokens = response.usage.completion_tokens
        t_tokens = response.usage.total_tokens

        # Accumulate metrics
        total_prompt_tokens += p_tokens
        total_comp_tokens += c_tokens

        # Calculate turn cost
        turn_cost = (
            (p_tokens / 1_000_000) * PRICE_PER_1M_PROMPT +
            (c_tokens / 1_000_000) * PRICE_PER_1M_COMPLETION
        )

        print(f"\nAda: {reply}\n")
        print(f"   [Tokens: {t_tokens} (P: {p_tokens}, C: {c_tokens}) | Turn Cost: ${turn_cost:.6f}]")
        print("-" * 65)

        # Append assistant reply to keep memory across turns
        messages.append({"role": "assistant", "content": reply})

    except RateLimitError:
        print("\n❌ Rate limit reached. Waiting 3 seconds before next input...\n")
        if messages and messages[-1]["role"] == "user":
            messages.pop()

    except APIError as e:
        print(f"\n❌ API Error: {e.message}\n")
        if messages and messages[-1]["role"] == "user":
            messages.pop()

    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}\n")
        if messages and messages[-1]["role"] == "user":
            messages.pop()

# 4. Final Session Analytics
all_tokens = total_prompt_tokens + total_comp_tokens
total_cost = (
    (total_prompt_tokens / 1_000_000) * PRICE_PER_1M_PROMPT +
    (total_comp_tokens / 1_000_000) * PRICE_PER_1M_COMPLETION
)

print("\n" + "=" * 65)
print("📊 SESSION USAGE & COST SUMMARY")
print("=" * 65)
print(f"Prompt Tokens:     {total_prompt_tokens:,}")
print(f"Completion Tokens: {total_comp_tokens:,}")
print(f"Total Tokens:      {all_tokens:,}")
print(f"Estimated Cost:    ${total_cost:.6f}")
print("=" * 65)
