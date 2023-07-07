from fastapi import APIRouter

from bson import ObjectId
from config.db import conn
from models.phone import Phone
from schemas.phone import phonesEntity, phoneEntity, phoneLogEntity

phone = APIRouter(prefix="/phone", tags=["Phone routes"])

@phone.get('')
async def find_all_phones():
    return phonesEntity(conn.dsi.telip.find())

@phone.post('')
async def create_phone(phone: Phone):
    create_event = conn.dsi.telip.insert_one(dict(phone))
    return phonesEntity(conn.dsi.telip.find())

@phone.get('/{id}')
async def find_one_phone(id):
    return phoneEntity(conn.dsi.telip.find_one({"_id": ObjectId(id)}))

@phone.put("/{id}")
async def update_phone(id, phone: Phone):
    conn.dsi.telip.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(phone)})
    return phoneEntity(conn.dsi.telip.find_one({"_id": ObjectId(id)}))

@phone.delete("/{id}")
async def delete_phone(id):
    return phoneEntity(conn.dsi.telip.find_one_and_delete({"_id": ObjectId(id)}))