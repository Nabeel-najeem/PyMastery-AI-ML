from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
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
    boot_time_timestap = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestap)
    system_boot_time =bt.strftime("%Y-%m-%d %H:%M:%S")
    physical_cores = psutil.cpu_count(logical=False)
    total_threads = psutil.cpu_count(logical=True)
    cpu_per_core = psutil.cpu_percent(interval=None, percpu=True)
    battery = psutil.sensors_battery()
    percentage = battery.percent if battery else "N/A"
    pluged = "pluged in" if battery and battery.power_plugged else "on battery"
    
    
    
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
            "disk_free": disk_free,
            "system_boot_time": system_boot_time,
            "physical_cores": physical_cores,
            "total_threads": total_threads,
            "cpu_per_core": cpu_per_core,
            "battery_status": f"{percentage}% ({pluged})"
        }
    )