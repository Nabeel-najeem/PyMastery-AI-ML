from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import psutil

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    ram_usage = f"{psutil.virtual_memory().percent}%"
    cpu_frequency = psutil.cpu_freq().current
    Disk_usage = f"{psutil.disk_usage('/').percent}%"
    
    net_io = psutil.net_io_counters()
    net_sent = f"{net_io.bytes_sent / (1024**2):.2f} MB"
    net_recv = f"{net_io.bytes_recv / (1024**2):.2f} MB"
    disk = psutil.disk_usage('/')
    disk_total = f"{disk.total / (1024**3):.2f} GB"
    disk_free = f"{disk.free / (1024**3):.2f} GB"
    
    
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "user_name": "Nabeel",
            "college": "Musaliar college",
            "ram_usage": ram_usage,
            "cpu_frequency": cpu_frequency,
            "Disk_usage": Disk_usage,
            "net_sent": net_sent,
            "net_recv": net_recv,
            "disk_total": disk_total,
            "disk_free": disk_free
            
        }
    )