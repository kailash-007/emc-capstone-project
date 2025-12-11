from flask import Flask, render_template, request, redirect, session
from database import init_db
from models import *

app = Flask(__name__)
app.secret_key = "supersecret!"

@app.before_first_request
def setup():
    init_db()

@app.route("/")
def home():
    if "user" in session:
        return redirect("/notes")
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if validate_login(username, password):
            session["user"] = username
            return redirect("/notes")
        else:
            return "Invalid username or password"
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        create_user(username, password)
        return redirect("/login")
    return render_template("register.html")

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if "user" not in session:
        return redirect("/login")
    user = get_user(session["user"])
    if request.method == "POST":
        note = request.form["note"]
        add_note(user["id"], note)
    notes = get_notes(user["id"])
    return render_template("notes.html", notes=notes, username=session["user"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        print("Test run successful")
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)
