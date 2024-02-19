from pydantic import BaseModel

class GuardianBase(BaseModel):
  id: int # Needs to be transformed to user_id
  name: str
  last_name: str
  email: str

class GuardianCreate(GuardianBase):
  pass
