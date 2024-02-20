from pydantic import BaseModel

class Family(BaseModel):
  id: int
  family_name: str

class GuardianMember(BaseModel):
  user_id: int
  name: str
  last_name: str
  email: str

class Child(BaseModel):
  id: int
  full_name: str
  family_id: int
