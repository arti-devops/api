# SCHEMA ENTITIES

def memberEntity(item) -> dict:
    return{

        "member_id": str(item["_id"]),
        "member_email": str(item["member_email"]),
        "member_gender": str(item["member_gender"]),
        "member_contact": str(item["member_contact"]),
        "member_fullname": str(item["member_fullname"]),
        "member_matricule": str(item["member_matricule"]),
        "member_positions": list([
            dict({
                "member_position_role": str(m["position_role"]),
                "member_position_date": str(m["position_date"]),
                "member_position_status": str(m["position_status"]),
                "member_position_service": str(m["position_service"]),
                "member_position_contrat": str(m["position_contrat"]),
                "member_position_division": str(m["position_division"]),
                "member_position_location": str(m["position_location"]),
                "member_position_category": str(m["position_category"]),
                "member_position_subdivision": str(m["position_subdivision"]),
            })
        ] for m in item["member_positions"])
    } 

def membersEntity(entity) -> list:
    return [memberEntity(item) for item in entity]