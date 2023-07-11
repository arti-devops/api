def deviceEntity(item) -> dict:
    return{
        "device_id":str(item["_id"]),
        "device_user":str(item["device_user"]),
        "device_type":str(item["device_type"]),
        "device_post_number":str(item["device_post_number"]),
        "device_brand_name":str(item["device_brand_name"]),
        "device_brand_model":str(item["device_brand_model"]),
        "device_ip_address":str(item["device_ip_address"]),
        "device_status":str(item["device_status"]),
        "device_serial_number":str(item["device_serial_number"]),
    }

def devicesEntity(entity) -> list:
    return [deviceEntity(item) for item in entity]