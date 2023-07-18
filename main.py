from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.modules.rh.routes.log import log
from src.modules.dsi.routes.device import device
from src.modules.dsesp.routes.project import project
from src.provider.routes.member import provider

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(provider)
app.include_router(log)
app.include_router(device)
app.include_router(project)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": {"details":exc.detail,"request":request}},
    )