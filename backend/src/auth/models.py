from sqlalchemy import Column, Integer, String, DateTime
from src.database.dbConnection import Base
import datetime

class User(Base):
  __tablename__ = "users"
  __table_args__ = {"schema": "auth"}

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  username = Column(String, unique=True, index=True)
  password = Column(String)
  name = Column(String)
  last_name = Column(String)
  createdAt_created = Column(DateTime, default=datetime.datetime.utcnow)
  updatedAt_updated = Column(DateTime, default=datetime.datetime.utcnow)

class AccessToken(Base):
  __tablename__ = "access_tokens"
  __table_args__ = {"schema": "auth"}

  access_token = Column(String, primary_key=True)
  user_id = Column(Integer, index=True)
  createdAt_created = Column(DateTime, default=datetime.datetime.utcnow)
  updatedAt_updated = Column(DateTime, default=datetime.datetime.utcnow)
