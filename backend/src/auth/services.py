from sqlalchemy.orm import Session
from src.auth.models import User, AccessToken
from jwt import encode
from src.config import config

def validate_user(db: Session, username: str, password: str):
  user = db.query(User).filter(User.username == username, User.password == password).first()
  if not user:
    return None
  
  return user

def create_access_token(db: Session, user_id: int):
  access_token = encode({ "user_id": user_id }, config["JWT_SECRET_KEY"], algorithm='HS256')
  db_access_token = AccessToken(access_token=access_token, user_id=user_id)
  db.add(db_access_token)
  db.commit()
  db.refresh(db_access_token)
  return db_access_token