from fastapi import APIRouter

from src.config.db import projectsdb
from src.modules.dsesp.schemas.project import projetsEntity

project = APIRouter(prefix="/projects", tags=["Projects list routes"])

@project.get('')
async def find_all_projects():
    return projetsEntity(projectsdb.find().limit(20))