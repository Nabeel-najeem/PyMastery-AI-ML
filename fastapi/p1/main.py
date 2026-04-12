from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello Hexer. Your  API is alive."}

@app.get("/status")
async def sattus():
    return {
        "Stusent" : "Nabeel",
        "Colleeg" : "MUsaliar",
        "Status" : "Ready for Ai"
        }




