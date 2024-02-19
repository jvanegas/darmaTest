from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
  username: str

class LoginUser(UserBase):
  password: str

class User(UserBase):
  model_config = ConfigDict(from_attributes=True) # This replace subclass Config with property orm_mode = True

  id: int
  username: str
  name: str
  last_name: str

class accessToken(BaseModel):
  access_token: str

class accessTokenCreate(accessToken):
  model_config = ConfigDict(from_attributes=True)

  user_id: str
