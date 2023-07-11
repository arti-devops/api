from fastapi import APIRouter

from src.config.db import logsdb
from src.modules.rh.schemas.log import logsEntity
from src.modules.rh.transmute.log import process_month_log_count, process_daily_logs

log = APIRouter(prefix="/logs", tags=["Logs list routes"])

@log.get('')
async def find_all_logs():
    return logsEntity(logsdb.find().limit(20))

@log.get("/dailylog/{ddate}")
async def get_members_daily_logs(ddate):
    return process_daily_logs(ddate)

@log.get('/mlc/{sdate}:{edate}')
async def get_member_month_late_count(sdate="2023-04-01", edate="2023-04-30"):
    return process_month_log_count(sdate, edate)