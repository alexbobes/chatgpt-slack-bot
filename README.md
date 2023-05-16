# Slack Bot using OpenAI's GPT-3 or GPT-4

This project includes a Slack bot that uses OpenAI's GPT-3 or GPT-4 model to respond to user messages. The bot listens for a `/chatgpt` command, sends the command's text to the GPT-3 API, and posts the model's response back to the Slack channel.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python 3.7+ installed on your system. You also need to install the necessary packages using pip:

```shell
pip install flask slack_sdk openai dotenv
```

### Setup

Clone the repository to your local machine.
Create a .env file in the root directory of the project and add the following environment variables:

```shell
OPENAI_API_KEY=<Your OpenAI API key>
SLACK_BOT_TOKEN=<Your Slack Bot User OAuth Token>
SLACK_APP_TOKEN=<Your Slack App-Level Token>
```
### Run the Flask application

```shell
python app.py
```
The bot is now ready to receive /chatgpt commands in the specified Slack channel.

### How It Works

When a /chatgpt command is posted in the Slack channel, the bot extracts the text from the command and sends it to the OpenAI API. The API's response is then posted back to the Slack channel.

The bot's response includes the user's original message, the AI's response, and a dashed line for clarity.