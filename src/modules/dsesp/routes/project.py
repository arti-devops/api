from fastapi import APIRouter

from src.config.db import projectsdb
from src.modules.dsesp.schemas.project import projectsEntity
from src.modules.dsesp.transmute.project import process_query_data
from src.modules.dsesp.models.project import ProjectResponse, FilterProject

project = APIRouter(prefix="/projects", tags=["Projects list routes"])

@project.get('')
async def find_all_projects():
    return projectsEntity(projectsdb.find().limit(20))

@project.post('/q', 
             description="Search Project by Direction name or filter by Direction Name and Status")
async def search_all_pojects(filter: FilterProject):
    return process_query_data(filter.filter)