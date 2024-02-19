from sqlalchemy import Column, Integer, String, DateTime, Time, Boolean
from src.database.dbConnection import Base
import datetime

class Activity(Base):
  __tablename__ = "activities"
  __table_args__ = {"schema": "activity"}

  id = Column(Integer, primary_key=True, index=True)
  child_id = Column(Integer)
  activity_name = Column(String)
  activity_weekday = Column(Integer)
  activity_start_time = Column(Time)
  activity_end_time = Column(Time)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.datetime.utcnow)

class ActivityHistory(Base):
  __tablename__ = "activities_history"
  __table_args__ = {"schema": "activity"}

  id = Column(Integer, primary_key=True, index=True)
  activity_id = Column(Integer)
  responsible_guardian_id = Column(Integer)
  is_completed = Column(Boolean)
  resolved_at = Column(DateTime, default=datetime.datetime.utcnow)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.datetime.utcnow)
