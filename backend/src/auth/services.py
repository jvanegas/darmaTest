from sqlalchemy.orm import Session
from logging import Logger
from src.auth.models import User, AccessToken
from jwt import encode
from src.config import config
from src.guardians.services import create_guardian
from datetime import datetime, timezone


def validate_user(db: Session, logger: Logger, username: str, password: str):
  logger.debug(f"Validating user {username}")
  user = db.query(User).filter(User.username == username, User.password == password).first()
  if not user:
    logger.info(f"User {username} not found")
    return None
  
  create_guardian(db, logger, user)
  
  return user

def create_access_token(db: Session, logger: Logger, user_id: int):
  access_token = encode({ "user_id": user_id, "exp": datetime.now(tz=timezone.utc) }, config["JWT_SECRET_KEY"], algorithm='HS256',)
  db_access_token = AccessToken(access_token=access_token, user_id=user_id)
  db.add(db_access_token)
  db.commit()
  db.refresh(db_access_token)
  return db_access_token