from pydantic import BaseModel

class Phone(BaseModel):
    user: str
    post_number: int
    brand: str
    brand_model: str
    ip_address: str
    status: str

class PhoneLog(BaseModel):
    log_id: str
    user: str
    post_number: int
    brand: str
    brand_model: str
    ip_address: str
    status: str
