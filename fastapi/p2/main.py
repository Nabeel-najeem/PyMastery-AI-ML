from fastapi import FastAPI
from pydantic import BaseModel
import psutil
import platform

class SystemStatus(BaseModel):
    user: str
    device_os: str
    ram_load: str
    status: str


class SystemEngine:
    def __init__(self):
        self.os= platform.system()
        self.processor = platform.processor()
        
    def get_ram_usage(self)  -> str:
        return f"{psutil.virtual_memory().percent}%"
    
app = FastAPI()
hexer_engine = SystemEngine()


@app.get("/status", response_model=SystemStatus)
async def status():
    return{
        "user" : "Nabeel",
        "device_os" : hexer_engine.os,
        "ram_load" : hexer_engine.get_ram_usage(),
        "status" : "Healthy"
    }

