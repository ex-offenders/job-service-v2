from sqlmodel import Session
from .database import engine
from fastapi import Request, HTTPException
import jwt

def get_session():
    with Session(engine) as session:
        yield session

def get_user_id_from_token(request: Request) -> str:
    token2 = request.headers.get("Authorization").split("Bearer ")[1]
    print(token2)
    payload2 = jwt.decode(token2, options={"verify_signature": False})
    user_id2: str = payload2.get("sub")
    print(payload2)
    print(user_id2)
    try:
        token = request.headers.get("Authorization").split("Bearer ")[1]
        payload = jwt.decode(token, options={"verify_signature": False})
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="User ID not found in token")
        return user_id
    except:
        raise HTTPException(status_code=401, detail="Could not validate credentials")