import hashlib
import datetime
from utils.crypto import sha256
from model.user import exists, set_token

def login_user(user_name, password):

    hashed_password = sha256(password)
    user_exists, user_id, db_password = exists(user_name)
    if not user_exists:
        return "error" if not user_exists else "success", "user does not exists"

    if hashed_password != db_password:
        return "error" if not user_exists else "success", "invalid password"

    now = datetime.datetime.now()
    token_expires_at = now + datetime.timedelta(hours=1)
    token = sha256(user_name + str(now))
    set_token(user_id, token, token_expires_at)

    return "error" if not user_exists else "success", {
        'token': token,
        'expires_at': token_expires_at
    }