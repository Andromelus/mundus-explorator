from flask import Flask
from flask import render_template
from flask import request
from controller.main_register import register_user
from controller.main_login import login_user

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    post_data = request.get_json()
    status, info = register_user(post_data["user_name"], post_data["password"])
    return {
        "status": status,
        "action": "register user",
        "info": info
    }

@app.route("/login", methods=["POST"])
def login():
    post_data = request.get_json()
    status, info = login_user(
        post_data["user_name"],
        post_data["password"]
    )
    return {
        "status": status,
        "action": "login user",
        "info": info
    }

@app.route("/game")
def game():
    return render_template("game.html")
