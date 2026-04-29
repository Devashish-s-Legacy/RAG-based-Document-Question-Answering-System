import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI RAG Assistant", layout="wide")

st.title("🤖 AI Copilot (RAG)")
st.write("Ask questions from your uploaded documents")

# Sidebar for upload
st.sidebar.header("📂 Upload Document")

uploaded_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{API_URL}/upload", files={"file": uploaded_file})

    if response.status_code == 200:
        st.sidebar.success("File uploaded & indexed!")
    else:
        st.sidebar.error("Upload failed")

# Chat section
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("💬 Ask a question")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        res = requests.post(
            f"{API_URL}/ask",
            json={"query": query}
        )

        if res.status_code == 200:
            data = res.json()
            answer = data.get("answer", "No answer")

            st.session_state.chat_history.append((query, answer))
        else:
            st.error("API error")

# Display chat
for q, a in reversed(st.session_state.chat_history):
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 AI:** {a}")
    st.markdown("---")