import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    messages.append("{}: {}".format(username, message))

@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "Welcome, {0} - {1}".format(username, messages)

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)