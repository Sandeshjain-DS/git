import streamlit as st
import anthropic
import os

# Set up the Streamlit app
st.title("Claude AI Chatbot Demo")
st.markdown("""
This is a simple demo showing how to use Claude AI with Streamlit.

**Note:** You'll need to provide your own Anthropic API key to use this application.
""")

# Sidebar for API key input
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your Anthropic API Key:", type="password")

# Initialize the Anthropic client if API key is provided
if api_key:
    client = anthropic.Anthropic(api_key=api_key)
else:
    st.warning("Please enter your Anthropic API Key in the sidebar to use the chatbot.")
    st.stop()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What is up?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Claude
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            with st.spinner("Thinking..."):
                response = client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1024,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                full_response = response.content[0].text
                message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            full_response = "Sorry, I encountered an error."

        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Clear chat button
if st.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()