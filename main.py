from fastapi import FastAPI
from routes.phone import phone

app = FastAPI()

app.include_router(phone)