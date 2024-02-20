from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
  username: str

class LoginUser(UserBase):
  password: str

class accessToken(BaseModel):
  access_token: str
