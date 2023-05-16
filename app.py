import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.context.say import Say
from threading import Thread
import openai

load_dotenv()

app = Flask(__name__)


api_key = os.environ.get('OPENAI_API_KEY')
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN = os.environ.get('SLACK_APP_TOKEN')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL')

openai.api_key = api_key

slack_app = App(token=SLACK_BOT_TOKEN)

@slack_app.command("/chatgpt")
def command(ack, say, command):
    # Acknowledge the command right away
    ack()

    # Extract the user's message
    text = command['text']

    # Query the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text}
        ]
    )

    # Extract the AI's response
    response_text = response['choices'][0]['message']['content']

    # Post the user's message and the response back to the same channel
    say(f"*Message:* {text}\n*Response:* {response_text}\n----------------")

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    # Start the socket mode handler
    handler = SocketModeHandler(slack_app, SLACK_APP_TOKEN)
    thread = Thread(target=handler.start)
    thread.start()
    
    # Start the Flask app
    app.run(port=3333)