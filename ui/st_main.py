import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Configuration
API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Lucy", page_icon="🤖", layout="wide")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    # Get session ID from API when app starts
    try:
        response = requests.get(f"{API_URL}/session", timeout=5)
        response.raise_for_status()
        st.session_state.session_id = response.json()["session_id"]
    except Exception as e:
        st.error(f"Failed to get session ID: {e}")
        st.stop()

# Title
st.title("🤖 Lucy")
st.markdown("---")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call API and get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    f"{API_URL}/chat",
                    json={"message": prompt, "session_id": st.session_state.session_id},
                    timeout=60,
                )
                response.raise_for_status()

                assistant_response = response.json()["response"]
                st.markdown(assistant_response)

                # Add assistant response to chat history
                st.session_state.messages.append(
                    {"role": "assistant", "content": assistant_response}
                )

            except requests.exceptions.RequestException as e:
                error_message = f"Error: {str(e)}"
                st.error(error_message)
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_message}
                )

# Sidebar with controls
with st.sidebar:
    st.header("Settings")

    st.caption(f"**Session ID:** {st.session_state.session_id[:8]}...")

    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown(f"**API Endpoint:** {API_URL}")
    st.markdown(f"**Total Messages:** {len(st.session_state.messages)}")
