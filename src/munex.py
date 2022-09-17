from flask import Flask
from flask import render_template
from flask import request
from controller.main_register import register_user

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    post_data = request.get_json()
    print(post_data)
    status, info = register_user(post_data["user_name"], post_data["password"])
    return {
        "status": status,
        "action": "register user",
        "info": info
    }