from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from logging import Logger
from typing import List
from src.dependencies import get_db, get_logger, validate_jwt, get_redis_connection
from src.families.dependencies import guardian_belongs_to_family
from src.families.schemas import Family, GuardianMember, Child
from src.activities.schemas import Activity, ActivityCreate
from src.families import services as families_services
from src.activities import services as activities_services

router = APIRouter()

@router.get("/", response_model=List[Family])
async def get_all_families (decoded_token = Depends(validate_jwt), db: Session = Depends(get_db), logger: Logger = Depends(get_logger)):
  logger.info(decoded_token)
  return families_services.get_all_families(db, logger, decoded_token["user_id"])

@router.get("/{family_id}/member", response_model=List[GuardianMember], dependencies=[Depends(guardian_belongs_to_family)])
async def get_family_members (family_id: int, db: Session = Depends(get_db), logger: Logger = Depends(get_logger)):
  return families_services.get_family_members(db, logger, family_id)

@router.get("/{family_id}/child", response_model=List[Child], dependencies=[Depends(guardian_belongs_to_family)])
async def get_family_children (family_id: int, db: Session = Depends(get_db), logger: Logger = Depends(get_logger)):
  return families_services.get_family_children(db, logger, family_id)

@router.post("/{family_id}/activity/", response_model=Activity, dependencies=[Depends(guardian_belongs_to_family)])
async def create_activity (family_id: int, activity: ActivityCreate, db: Session = Depends(get_db), logger: Logger = Depends(get_logger), redis = Depends(get_redis_connection)):
  return await activities_services.create_activity(db, logger, redis, family_id, activity)