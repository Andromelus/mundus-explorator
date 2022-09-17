import hashlib

def sha256(value):
    return hashlib.sha256(
        value.encode("utf-8")
    ).hexdigest()