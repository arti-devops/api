from typing import List
from pydantic import BaseModel, Field

class MemberPosition(BaseModel):
    member_position_role: str 
    member_position_date: str
    member_position_status: str 
    member_position_service: str 
    member_position_contrat: str
    member_position_division: str 
    member_position_location: str 
    member_position_category: str
    member_position_subdivision: str 

class Member(BaseModel):
    member_email: str
    member_gender: str
    member_contact: str
    member_fullname: str
    member_matricule: str
    member_positions: List[MemberPosition]