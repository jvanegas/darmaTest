from sqlalchemy import Column, Integer, String, DateTime
from src.database.dbConnection import Base
import datetime

class Child(Base):
  __tablename__ = "children"
  __table_args__ = {"schema": "activity"}

  id = Column(Integer, primary_key=True, index=True)
  full_name = Column(String)
  family_id = Column(String)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.datetime.utcnow)

class Family(Base):
  __tablename__ = "families"
  __table_args__ = {"schema": "activity"}

  id = Column(Integer, primary_key=True, index=True)
  family_name = Column(String)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.datetime.utcnow)

class FamilyMember(Base):
  __tablename__ = "family_members"
  __table_args__ = {"schema": "activity"}

  id = Column(Integer, primary_key=True, index=True)
  guardian_id = Column(Integer)
  children_id = Column(Integer)
  family_id = Column(Integer)
  relationship_type = Column(String)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.datetime.utcnow)
