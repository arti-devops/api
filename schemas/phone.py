def phoneEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "user":str(item["user"]),
        "post_number":int(item["post_number"]),
        "brand":str(item["brand"]),
        "brand_model":str(item["brand_model"]),
        "ip_address":str(item["ip_address"]),
        "status":str(item["status"]),
    }

def phoneLogEntity(item) -> dict:
    phone_entity = phoneEntity(item) 
    phone_log_entity = dict(phone_entity)
    phone_log_entity["log_id"] = str(item["_id"])
    return phone_log_entity

def phonesEntity(entity) -> list:
    return [phoneEntity(item) for item in entity]

def phonesLogEntity(entity) -> list:
    return [phoneLogEntity(item) for item in entity]