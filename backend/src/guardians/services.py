from sqlalchemy.orm import Session
from src.guardians.models import Guardian
from src.guardians.schemas import GuardianCreate
from logging import Logger

def create_guardian(db: Session, logger: Logger, user: GuardianCreate):
  logger.debug(f"Creating guardian for user {user.id}")
  guardian_exists = get_guardian_by_user_id(db, user.id)

  if guardian_exists:
    logger.info(f"Guardian for user {user.id} already exists")
    return guardian_exists
  
  db_guardian = Guardian(
    user_id=user.id,
    name=user.name,
    last_name=user.last_name,
    email= user.email
  )
  db.add(db_guardian)
  db.commit()
  db.refresh(db_guardian)
  logger.info(f"Guardian for user {user.id} created")
  return db_guardian

def get_guardian_by_user_id(db: Session, user_id: int):
  return db.query(Guardian).filter(Guardian.user_id == user_id).first()
