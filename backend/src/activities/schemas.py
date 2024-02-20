from pydantic import BaseModel
from datetime import time

class Activity (BaseModel):
  id: int
  child_id: int
  family_id: int
  activity_name: str
  activity_weekday: int
  activity_start_time: time
  activity_end_time: time

class ActivityCreate(BaseModel):
  child_id: int
  activity_name: str
  activity_weekday: int # Between 0 to 6, 0: monday and 6: sunday
  activity_start_time: str
  activity_end_time: str
