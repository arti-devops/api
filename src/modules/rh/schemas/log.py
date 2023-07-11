def logEntity(item) -> dict:
    return{
        "log_id": str(item["_id"]),
        "log_date": str(item["log_date"].date()),
        "log_checkin": str(item["log_checkin"].time()),  
        "log_checkout": str(item["log_checkout"].time()),
        "log_member_id": str(item["log_member_id"]),
        "log_member_name": str(item["log_member_name"]),
        "log_count": int(item["log_count"])
    }

def abCountEntity(item) -> dict:
    return{
        "log_member_id": str(item["_id"]),
        "log_member_name": str(item["log_member_name"]),
        "log_month_count": int(item["log_month_count"])
    }

def lateCountEntity(item) -> dict:
    return{
        "log_member_id": str(item["_id"]),
        "log_member_name": str(item["log_member_name"]),
        "log_month_late_count": int(item["log_month_late_count"])
    }

def logsEntity(entity) -> list:
    return [logEntity(item) for item in entity]

def absCountEntity(entity) -> dict:
    return [abCountEntity(item) for item in entity]

def latesCountEntity(entity) -> dict:
    return [lateCountEntity(item) for item in entity]