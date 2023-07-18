from src.modules.dsi.models.options import ListOptions
from pydantic import BaseModel, Field, validator

class Device(BaseModel):
    device_name: str = Field(default="Color Laserjet Pro", description="Device name")
    device_user: str = Field(default="Al-Karid", description="Device user")
    device_type: str = Field(default="TELEPHONE IP", description="Device type")
    device_login: str = Field(default="NO", description="Device login")
    device_status: str = Field(default="offline", description="Device status")
    device_password: str = Field(default="NO", description="Device password")
    device_hostname: str = Field(default="IP-DSI", description="Device hostname")
    device_brand_name: str = Field(default="Yealink", description="Device brand name")
    device_ip_address: str = Field(default="192.168.0.220", description="Device IP address")
    device_post_number: int = Field(default=711, description="Device post number")
    device_brand_model: str = Field(default="T33G", description="Device brand model")
    device_serial_number: str = Field(default="VNC00015LK", description="Device serial number")
    device_connexion_mode: str = Field(default="CABLE", description="Device connexion mode")

class DeviceFilter(BaseModel):
    q: str = Field(default="", description="Search by value")
    dtype: str = Field(default="", description="Device Type filter")
    brand: str = Field(default="", description="Device Brand filter")
    status: str = Field(default="", description="Device Status filter")
    options: ListOptions = ListOptions()

    @validator('brand', 'status', pre=True)
    def set_default_if_null(cls, v):
        if v is None:
            return ""
        return v

class PostDevice(BaseModel):
    device: Device = Device()

class FilterDevice(BaseModel):
    filter : DeviceFilter = DeviceFilter()