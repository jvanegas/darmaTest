from sqlalchemy.orm import Session
from aioredis import Redis
from logging import Logger
from src.activities.schemas import ActivityCreate
from src.activities.models import Activity
from src.families.services import get_family_members
from src.families.schemas import GuardianMember
from typing import List
from urllib import parse

async def create_activity(db: Session, logger: Logger, redis: Redis, family_id: int, activity: ActivityCreate):
  db_activity = Activity(**activity.model_dump(), family_id=family_id)
  db.add(db_activity)
  db.commit()
  db.refresh(db_activity)
  await program_activity(logger, redis, db_activity.id) # Should we wait? Or just fire and forget?
  db_members = get_family_members(db, logger, family_id)
  send_emails(logger, db_members, db_activity)
  return db_activity

async def program_activity(logger: Logger, redis: Redis, activity_id: int):
  # TODO: calculate the expire time based on the activity weekday and time
  await redis.set(activity_id, "programmed", 60) #  Expire in 60 seconds

def send_emails(logger: Logger, members: List[GuardianMember], activity: Activity):
  for m in members:
    logger.info(f"Sending email to {m.email}")

  week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  logger.info(f"Activity {activity.activity_name} programmed for {week_days[activity.activity_weekday]} at {activity.activity_start_time} to {activity.activity_end_time} every week")
  urlencode = parse.urlencode({
    "action": "TEMPLATE",
    "text": activity.activity_name,
    "dates": "20210101T000000Z/20210101T010000Z"
  })
  link = f'https://calendar.google.com/calendar/render?{urlencode}'
  # For now, only Gmail
  # TODO: use redirect to send to the correct calendar app and collect metrics of calendars used by the guardians
  logger.info(f"Calendar link: {link}")

