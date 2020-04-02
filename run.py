import os
from datetime import datetime #imports the datetime module from python's standard library
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_messages(username, message):
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S") #%H is the hour in 24h format, %M is for the minutes, %S is for the seconds. The now() method gets the current time
    messages_dict = {"timestamp": now, "from": username, "message": message} #messages_dict is a dictionary that stores our now, username and message variables
    messages.append(messages_dict) #displays date, username and then message

@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    
    if request.method == "POST":
        session["username"] = request.form["username"] #sets the username variable to the username given in the index.html form
    
    if "username" in session: #if the "username" variable is set
        return redirect(session["username"]) #instead of redirecting to index.html, we are going to redirect to the session "username" - e.g. the @app.route("username")
    
    return render_template("index.html")


@app.route("/<username>", methods=["GET", "POST"])
def user(username):
    """Display chat messages"""
    
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_messages(username, message)
        return redirect(session["username"]) #resends the username each time the page is refreshed
    
    return render_template("chat.html", username = username, chat_messages = messages) #the username in chat.html is equal to the username variable in run.py, and the chat_messages in chat.html is equal to the messages list in run.py

@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host=os.getenv("IP", '0.0.0.0'), port=int(os.getenv("PORT", 5000)), debug=True)