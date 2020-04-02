import os
from datetime import datetime #imports the datetime module from python's standard library
from flask import Flask, redirect, render_template

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S") #%H is the hour in 24h format, %M is for the minutes, %S is for the seconds. The now() method gets the current time
    messages.append("({}) {}: {}".format(now, username, message)) #displays date, username and then message

def get_all_messages():
    """Get all of the messages and seperate using a <br> tag"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main page with instructions"""
    return render_template("index.html")


@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)