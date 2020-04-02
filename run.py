import os
from datetime import datetime #imports the datetime module from python's standard library
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "randomstring123")
messages = []

def add_message(username, message):
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S") #%H is the hour in 24h format, %M is for the minutes, %S is for the seconds. The now() method gets the current time
    messages.append({"timestamp": now, "from": username, "message": message}) #displays date, username and then message

@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    
    if request.method == "POST":
        session["username"] = request.form["username"] #sets the username variable to the username given in the index.html form
    
    if "username" in session: #runs if the "username" variable is set
        return redirect(url_for("user", username=session["username"]))
        
    return render_template("index.html")


@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    """Add and display chat messages"""
    
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"])) #resends the username each time the page is refreshed
    
    return render_template("chat.html", username = username, chat_messages = messages) #the username in chat.html is equal to the username variable in run.py, and the chat_messages in chat.html is equal to the messages list in run.py

app.run(host=os.getenv("IP", '0.0.0.0'), port=int(os.getenv("PORT", 5000)), debug=False)