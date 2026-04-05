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
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "user_name": "Nabeel",
            "college": "Musaliar college",
            "ram_usage": ram_usage,
            "cpu_frequency": cpu_frequency,
            "Disk_usage": Disk_usage
        }
    )