from sqlalchemy.orm import Session
from logging import Logger
from src.families.models import Family, FamilyMember, Child
from src.guardians.services import get_guardian_by_user_id


def get_all_families(db: Session, logger: Logger, user_id: int):
  members = db.query(FamilyMember).filter(FamilyMember.guardian_id == user_id).all()
  families = []
  for m in members:
    family = db.query(Family).filter(Family.id == m.family_id).first()
    families.append(family)

  return families

def get_family_members(db: Session, logger: Logger, family_id: int):
  families = db.query(FamilyMember).filter(FamilyMember.family_id == family_id).all()
  members = []
  for f in families:
    guardian = get_guardian_by_user_id(db, f.guardian_id)
    members.append(guardian)

  return members

def get_family_children(db: Session, logger: Logger, family_id: int):
  return db.query(Child).filter(Child.family_id == family_id).all()

