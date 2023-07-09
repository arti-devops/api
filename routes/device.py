from fastapi import APIRouter

from bson import ObjectId
from config.db import devicesdb
from transmute.device import process_query_data
from schemas.device import devicesEntity, deviceEntity
from models.device import PostDevice, FilterDevice

device = APIRouter(prefix="/devices", tags=["Devices CRUD routes"])

@device.get('', tags=["Devices List"])
async def find_all_devices():
    return devicesEntity(devicesdb.find())

@device.post('')
async def create_device(device: PostDevice):
    devicesdb.insert_one(dict(device.device))
    return devicesEntity(devicesdb.find())

@device.post('/q',  
             description="Search device by User name or filter by Brand and Status", tags=["Devices List"])
async def search_all_devices(filter: FilterDevice):
    return process_query_data(filter.filter)

@device.get('/{id}')
async def find_one_device(id):
    return deviceEntity(devicesdb.find_one({"_id": ObjectId(id)}))

@device.put("/{id}")
async def update_device(id, device: PostDevice):
    devicesdb.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(device.device)})
    return deviceEntity(devicesdb.find_one({"_id": ObjectId(id)}))

@device.delete("/{id}")
async def delete_device(id):
    return deviceEntity(devicesdb.find_one_and_delete({"_id": ObjectId(id)}))