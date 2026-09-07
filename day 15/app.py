"""
Task 4: Streamlit Web UI Chatbot
Run with: streamlit run app.py
Features:
- Web-based chat UI using st.chat_message and st.chat_input
- Dynamic conversation history tracking in st.session_state
- Sidebar tracking real-time token usage and cost metrics
- Memory reset button
"""

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# 1. Page Configuration
st.set_page_config(
    page_title="AI Mentor Chatbot",
    page_icon="🤖",
    layout="wide"
)

# 2. Setup Client
load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
base_url = "https://api.groq.com/openai/v1" if os.getenv("GROQ_API_KEY") else None

if not api_key:
    st.error("⚠️ No API Key found! Please set GROQ_API_KEY or OPENAI_API_KEY in your .env file.")
    st.stop()

client = OpenAI(api_key=api_key, base_url=base_url)
model_name = "openai/gpt-oss-120b" if base_url else "gpt-4o-mini"

PRICE_PER_1M_PROMPT = 0.15
PRICE_PER_1M_COMPLETION = 0.60

# 3. Session State (In-memory web state)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a concise, friendly AI Engineering mentor named Ada. Explain concepts clearly and concisely using markdown."
        }
    ]

if "total_prompt_tokens" not in st.session_state:
    st.session_state.total_prompt_tokens = 0

if "total_comp_tokens" not in st.session_state:
    st.session_state.total_comp_tokens = 0


# 4. Sidebar: Cost & Token Tracking
with st.sidebar:
    st.title("⚙️ Session Controls")

    total_tokens = st.session_state.total_prompt_tokens + st.session_state.total_comp_tokens
    total_cost = (
        (st.session_state.total_prompt_tokens / 1_000_000) * PRICE_PER_1M_PROMPT +
        (st.session_state.total_comp_tokens / 1_000_000) * PRICE_PER_1M_COMPLETION
    )

    st.metric("Total Tokens", f"{total_tokens:,}")
    st.metric("Estimated Cost", f"${total_cost:.6f}")
    st.caption(f"Model: `{model_name}`")

    # Clear Chat History Button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "system",
                "content": "You are a concise, friendly AI Engineering mentor named Ada. Explain concepts clearly and concisely using markdown."
            }
        ]
        st.session_state.total_prompt_tokens = 0
        st.session_state.total_comp_tokens = 0
        st.rerun()


# 5. Main Chat Interface
st.title("🤖 AI Engineering Mentor (Ada)")
st.caption("Ask questions about Python, LLMs, Prompt Engineering, or APIs!")

# Display message history (ignoring system prompt)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


# 6. User Input Handling (Event-driven)
user_prompt = st.chat_input("Ask a question...")

if user_prompt:
    # 1. Immediately render user question
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # 2. Append to session history
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # 3. Stream/display AI response
    with st.chat_message("assistant"):
        with st.spinner("Ada is thinking..."):
            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=st.session_state.messages,
                    temperature=0.7
                )

                reply = response.choices[0].message.content
                st.markdown(reply)

                # Save assistant response to history
                st.session_state.messages.append({"role": "assistant", "content": reply})

                # Update token tracking
                st.session_state.total_prompt_tokens += response.usage.prompt_tokens
                st.session_state.total_comp_tokens += response.usage.completion_tokens

                st.rerun()

            except Exception as e:
                st.error(f"❌ API Error: {str(e)}")
                if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
                    st.session_state.messages.pop()
