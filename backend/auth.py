import jwt
import datetime
from flask import request, jsonify
from backend.config import Config

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")

def verify_token():
    token = request.headers.get("Authorization")
    if not token:
        return None
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except:
        return None 
