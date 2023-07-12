from src.utils.validate_schema import *

def deviceEntity(item) -> dict:
    return{
        "device_id":str(item["_id"]),
        "device_user":validate_schema_str_attr(item,"device_user"),
        "device_type":validate_schema_str_attr(item,"device_type"),
        "device_post_number":validate_schema_int_attr(item,"device_post_number"),
        "device_brand_name":validate_schema_str_attr(item,"device_brand_name"),
        "device_brand_model":validate_schema_str_attr(item,"device_model_name"),
        "device_ip_address":validate_schema_str_attr(item,"device_ip_address"),
        "device_status":validate_schema_str_attr(item,"device_status"),
        "device_serial_number":validate_schema_str_attr(item,"device_serial_number")
    }

def devicesEntity(entity) -> list:
    return [deviceEntity(item) for item in entity]