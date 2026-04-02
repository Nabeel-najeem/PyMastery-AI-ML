from fastapi import FastAPI
import psutil
import platform

class SystemEngine:
    def __init__(self):
        self.os= platform.system()
        self.processor = platform.processor()
        
    def get_ram_usage(self)  -> str:
        return f"{psutil.virtual_memory().percent}%"
    
app = FastAPI()
hexer_engine = SystemEngine()

@app.get("/")
async def root():
    return {"message" : "Hello Hexer. Your  API is alive"}

@app.get("/status")
async def sattus():
    return{
        "user" : "Nabeel",
        "device os" : hexer_engine.os,
        "ram load" : hexer_engine.get_ram_usage(),
        "Status" : "Healthy"
    }
