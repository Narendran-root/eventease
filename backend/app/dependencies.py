# dependencies.py
from fastapi import Depends, HTTPException, Header
from app.auth import decode_token

async def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(401, "Missing Authorization header")
    token = authorization.replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        raise HTTPException(401, "Invalid token")
    return payload
