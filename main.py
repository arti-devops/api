from fastapi import FastAPI
from src.modules.rh.routes.log import log
from src.modules.dsi.routes.device import device
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(log)
app.include_router(device)