from fastapi import Depends, HTTPException
from src.dependencies import get_db, get_logger, validate_jwt
from sqlalchemy.orm import Session
from logging import Logger
from src.families import services

def guardian_belongs_to_family(family_id: int, decoded_token = Depends(validate_jwt), db: Session = Depends(get_db), logger: Logger = Depends(get_logger)):
  member = db.query(services.FamilyMember).filter(services.FamilyMember.guardian_id == decoded_token["user_id"], services.FamilyMember.family_id == family_id).first()
  if not member:
    raise HTTPException(status_code=404, detail="Family not found for guardian")
