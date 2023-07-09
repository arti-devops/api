from models.options import ListOptions
from pydantic import BaseModel, Field, validator

class Device(BaseModel):
    device_user: str
    device_type: str
    device_brand_name: str
    device_status: str
    device_ip_address: str
    device_device_type: str
    device_post_number: int
    device_brand_model: str
    device_serial_number: str

  
class DeviceFilter(BaseModel):
    q: str = Field(default="", description="Search by value")
    brand: str = Field(default="", description="Brand filter")
    status: str = Field(default="", description="Status filter")
    options: ListOptions = ListOptions()

    @property
    def offset(self):
        return (self.page - 1) * self.itemsPerPage
    
    @validator('brand', 'status', pre=True)
    def set_default_if_null(cls, v):
        if v is None:
            return ""
        return v