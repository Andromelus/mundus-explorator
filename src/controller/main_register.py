import hashlib
import logging
from model.user import create_user

def register_user(user_name: str, password: str):
    if user_name == "" or password == "":
        logging.error("empty name or password")
        return "error", "invalid user_name or password"

    hashed_password = hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()

    status = create_user(user_name, hashed_password)
    if status:
        return "success", None
    return "error", "something went wrong"