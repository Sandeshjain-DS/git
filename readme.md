# Claude AI Streamlit Demo

This is a simple demonstration of how to integrate Claude AI with a Streamlit application.

## Prerequisites

1. Python 3.7 or higher
2. An Anthropic API key (get one from [Anthropic Console](https://console.anthropic.com/))

## Installation

1. Clone this repository or download the files
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run claude_streamlit_app.py
   ```

2. Enter your Anthropic API key in the sidebar when the app starts
3. Start chatting with Claude!

## Features

- Simple chat interface with Claude AI
- Chat history persistence during the session
- Clear chat history button
- Error handling for API issues

## How It Works

The application uses the Anthropic Python SDK to communicate with Claude AI:
1. User enters their API key in the sidebar
2. User types messages in the chat input
3. Messages are sent to Claude AI via the API
4. Responses are displayed in the chat interface

## Deployment Options

### Local Deployment
Simply run `streamlit run claude_streamlit_app.py` locally.

### Cloud Deployment
You can deploy this app to various cloud platforms:
- Streamlit Community Cloud
- Heroku
- AWS
- Google Cloud Platform
- Azure

For Streamlit Community Cloud:
1. Push your code to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select your repository and branch
5. Deploy!

## Security Note

Never commit your API key to version control. The app is designed to accept the API key through user input for security.