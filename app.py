import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

import os
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Set up Streamlit page
st.set_page_config(page_title="Aira Conversational AI", page_icon="🤖", layout="centered")
st.title("🤖 Aira Conversational AI")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Display past messages
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").markdown(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").markdown(msg.content)

# User input
user_input = st.chat_input("Say something...")
if user_input:
    # Append user message
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.chat_message("user").markdown(user_input)

    # Get response from Gemini
    result = llm.invoke(st.session_state.chat_history)
    response = result.content

    # Append AI response
    st.session_state.chat_history.append(AIMessage(content=response))
    st.chat_message("assistant").markdown(response)

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: transparent;
        text-align: center;
        padding: 10px;
        font-size: 0.875rem;
        color: #888;
        z-index: 100;
    }
    </style>
    <div class="footer">
        Built by <a href='https://www.fuera.in.net/' target='_blank' style='color: inherit; text-decoration: underline;'><strong>FUERA</strong></a>
    </div>
    """,
    unsafe_allow_html=True
)
