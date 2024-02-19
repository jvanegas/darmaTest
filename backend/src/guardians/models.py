from sqlalchemy import Column, Integer, String, DateTime
from src.database.dbConnection import Base
import datetime

class Guardian(Base):
  __tablename__ = "guardians"
  __table_args__ = {"schema": "activity"}

  user_id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  last_name = Column(String)
  email = Column(String, nullable=True)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.datetime.utcnow)
