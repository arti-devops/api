from fastapi import APIRouter

from src.config.db import membersdb
from src.provider.schema.member import provideMembersEntity

provider = APIRouter(prefix="/provider", tags=["Proiver"])

@provider.get('/form/members')
async def provide_members():
    return provideMembersEntity(membersdb.find().sort("member_fullname", 1))