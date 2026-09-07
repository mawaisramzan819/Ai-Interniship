"""
Task 2: Parameter Exploration
- Systematic testing of Temperature (0.0 vs 0.7 vs 1.4) across repeated runs
- Experimenting with Max Tokens & Truncation (15 vs 50 vs 150)
- Top-p (Nucleus Sampling) evaluation (0.1 focused vs 0.9 diverse)
- Structured comparison summary
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
base_url = "https://api.groq.com/openai/v1" if os.getenv("GROQ_API_KEY") else None

client = OpenAI(api_key=api_key, base_url=base_url)
model_name = "openai/gpt-oss-120b" if base_url else "gpt-4o-mini"

# ==============================================================================
# 1. TEMPERATURE EXPLORATION (Same prompt, multiple runs)
# ==============================================================================
print("=" * 70)
print("EXPERIMENT 1: TEMPERATURE VARIATION (Testing Determinism vs Creativity)")
print("=" * 70)

test_prompt = "Generate 3 creative names for an AI cybersecurity startup."

for temp in [0.0, 0.7, 1.4]:
    print(f"\n--- Temperature: {temp} ---")
    for run in range(2):
        res = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": test_prompt}],
            temperature=temp,
            max_tokens=60
        )
        print(f"Run {run + 1}: {res.choices[0].message.content.strip().replace(chr(10), ' | ')}")


# ==============================================================================
# 2. MAX_TOKENS & TRUNCATION EXPLORATION
# ==============================================================================
print("\n" + "=" * 70)
print("EXPERIMENT 2: MAX_TOKENS & TRUNCATION BEHAVIOR")
print("=" * 70)

story_prompt = "Explain how transformer neural networks process language in simple terms."

for token_limit in [15, 40, 150]:
    res = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": story_prompt}],
        max_tokens=token_limit
    )
    finish_reason = res.choices[0].finish_reason
    output_text = res.choices[0].message.content.strip()
    
    print(f"\n[Limit: {token_limit} tokens | Finish Reason: '{finish_reason}']")
    print(f"Output: {output_text}")
    print(f"Tokens Used: Completion={res.usage.completion_tokens}, Total={res.usage.total_tokens}")


# ==============================================================================
# 3. TOP_P (NUCLEUS SAMPLING) EXPLORATION
# ==============================================================================
print("\n" + "=" * 70)
print("EXPERIMENT 3: TOP_P SAMPLING (0.1 Focused vs 0.9 Diverse)")
print("=" * 70)

analogy_prompt = "Write a creative analogy: Learning Python is like..."

for p in [0.1, 0.9]:
    print(f"\n[Top_p = {p}]")
    for run in range(2):
        res = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": analogy_prompt}],
            temperature=1.0,
            top_p=p,
            max_tokens=50
        )
        print(f"Run {run + 1}: {res.choices[0].message.content.strip()}")


# ==============================================================================
# 4. SUMMARY COMPARISON TABLE
# ==============================================================================
print("\n" + "=" * 70)
print("PARAMETER COMPARISON TABLE")
print("=" * 70)
print(f"{'Parameter':<15} | {'Range':<10} | {'Low Value Effect':<22} | {'High Value Effect':<22}")
print("-" * 75)
print(f"{'temperature':<15} | {'0.0 - 2.0':<10} | {'Deterministic, repeatable':<22} | {'Creative, unpredictable':<22}")
print(f"{'max_tokens':<15} | {'1 - N':<10} | {'Truncation mid-sentence':<22} | {'Complete response':<22}")
print(f"{'top_p':<15} | {'0.0 - 1.0':<10} | {'Considers top % tokens':<22} | {'Considers wider choices':<22}")
print("=" * 70)
