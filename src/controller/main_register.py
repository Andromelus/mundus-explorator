import hashlib
import logging
from model.user import create_user
from utils.crypto import sha256

def register_user(user_name: str, password: str):
    if user_name == "" or password == "":
        logging.error("empty name or password")
        return "error", "invalid user_name or password"

    hashed_password = sha256(password)

    status = create_user(user_name, hashed_password)
    if status:
        return "success", None
    return "error", "something went wrong"