from typing import Optional
from pydantic import BaseModel, Field

class Log(BaseModel):
    log_date: str = Field(default="2023-07-10", description="Date the member logged") 
    log_checkin: str = Field(default="08:07:00", description="First time the member logged in") 
    log_checkout: str = Field(default="21:10:00", description="Last time the member logged out") 
    log_member_id: str = Field(default="1080720A", description="Member's login card ID") 
    log_member_name: str = Field(default="CISSE Alassane", description="Member's name")
    log_count: str = Field(default=10, description="Number of times member loggin/out in a day")

class LogArrival(BaseModel):
    log_time: str = Field(default="2023-07-10", description="Date the member logged")
    log_member_id: str = Field(default="1080720A", description="Member's login card ID")
    log_member_name: str = Field(default="CISSE Alassane", description="Member's name")
    log_count: int = Field(default=0, description="Number of times member loggin/out in a day")
    log_time_islate: Optional[bool] = Field(None, description="Log time is late")

