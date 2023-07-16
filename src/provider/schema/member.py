# SCHEME MEMBER ENTITY

def provideMemberEntity(item) -> dict:
    return{
        "member_matricule": str(item["member_matricule"]),
        "member_fullname": str(item["member_fullname"]),
    }

def provideMembersEntity(entity) -> list:
    return [provideMemberEntity(item) for item in entity]