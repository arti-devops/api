from fastapi import APIRouter

from config.db import logsdb
from rh.schemas.log import logsEntity

log = APIRouter(prefix="/logs", tags=["Logs list routes"])

@log.get('')
async def find_all_logs():
    return logsEntity(logsdb.find().limit(20))