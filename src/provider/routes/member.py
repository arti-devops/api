from fastapi import APIRouter

from src.config.db import membersdb
from src.provider.schema.member import provideMembersEntity
from src.provider.models.printer import PostPrinter
from src.provider.transmute.device_printer import printer_status

provider = APIRouter(prefix="/provider", tags=["Provider"])

@provider.get('/form/members')
async def provide_members():
    return provideMembersEntity(membersdb.find().sort("member_fullname", 1))

@provider.post('/status/printers')
async def provide_printers_status(printers: PostPrinter):
    ip_list = [printer.ip for printer in printers.printers]
    return printer_status(ip_list)
    #return ip_list