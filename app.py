import streamlit as st
from gradio_client import Client

# Initialize the Gradio Client for the model
client = Client("Nitin111/meta-llama-Llama-3.2-3B-Instruct")

# Streamlit page configuration
st.set_page_config(page_title="Chatbot", page_icon="🤖")

# Create a title for the Streamlit app
st.title("Chatbot - Ask me anything!")

# Store conversation history in session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []


# Function to handle sending and receiving messages
def send_message():
    # Get the user's input from the text input box
    user_input = st.session_state.user_input
    if user_input:
        # Display the user's message
        st.session_state.conversation.append({"sender": "User", "message": user_input})

        # Get the bot's response
        result = client.predict(message=user_input, api_name="/chat")
        st.session_state.conversation.append({"sender": "Bot", "message": result})

        # Clear the input box for the next message
        st.session_state.user_input = ""


# Chat UI
for message in st.session_state.conversation:
    if message["sender"] == "User":
        st.markdown(f"**You**: {message['message']}")
    else:
        st.markdown(f"**Bot**: {message['message']}")

# Input box for the user to type messages
st.text_input("Type your message...", key="user_input", on_change=send_message)
