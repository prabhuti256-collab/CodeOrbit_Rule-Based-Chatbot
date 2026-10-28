
import streamlit as st
from chatbot import chatbot_response

st.set_page_config(
    page_title="PyBot AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Main heading
st.title("PyBot - AI Chatbot")
st.caption("Your simple rule-based AI assistant")

st.write(
    "Hello! I am PyBot. Ask me about Python, "
    "Artificial Intelligence, or greetings."
)

# Sidebar
with st.sidebar:
    st.header("About PyBot")
    st.write(
        "PyBot is a rule-based chatbot built with "
        "Python and Streamlit."
    )

    st.subheader("Features")
    st.write("- Greeting detection")
    st.write("- Python information")
    st.write("- Artificial Intelligence information")
    st.write("- Conversation history")

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! I'm PyBot. How can I help you?"
            }
        ]
        st.rerun()

# Initialize conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm PyBot. How can I help you?"
        }
    ]

# Display conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = chatbot_response(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)

# Footer
st.divider()
st.caption("PyBot | AI Internship Project")


