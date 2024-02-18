from fastapi import APIRouter, Depends, HTTPException
from src.dependencies import get_db, get_logger
from sqlalchemy.orm import Session
from src.auth.schemas import LoginUser, accessToken
from src.auth.services import validate_user, create_access_token

router = APIRouter()

@router.post("/login", response_model=accessToken)
async def login (user: LoginUser, db: Session = Depends(get_db), logger = Depends(get_logger)):
  userExists = validate_user(db, user.username, user.password)
  if not userExists:
    raise HTTPException(status_code=401, detail="Invalid username or password")
  db_access_token = create_access_token(db, userExists.id)
  return { "access_token": db_access_token.access_token }