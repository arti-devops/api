from fastapi import APIRouter

from bson import ObjectId
from src.config.db import projectsdb
from src.modules.dsesp.transmute.project import process_query_data
from src.modules.dsesp.schemas.project import projectEntity, projectsEntity
from src.modules.dsesp.models.project import FilterProject, UpdateProject, PostProject

project = APIRouter(prefix="/projects", tags=["Projects list routes"])

@project.get('')
async def find_all_projects():
    return projectsEntity(projectsdb.find().limit(20))

@project.get('/{id}')
async def find_one_project(id):
    return projectEntity(projectsdb.find_one({"_id": ObjectId(id)}))

@project.post('/q', 
             description="Search Project by Direction name or filter by Direction Name and Status")
async def search_all_pojects(filter: FilterProject):
    return process_query_data(filter.filter)

@project.post('', description="Create a new project")
async def create_project(project: PostProject):
    r = projectsdb.insert_one(project.project.model_dump())
    return projectEntity(projectsdb.find_one({"_id": r.inserted_id}))

@project.put('/{id}')
async def update_project(id, update: UpdateProject):
    projectsdb.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(update.update)})
    return projectEntity(projectsdb.find_one({"_id": ObjectId(id)}))

@project.delete('/{id}')
async def delete_project(id):
    return projectEntity(projectsdb.find_one_and_delete({"_id": ObjectId(id)}))