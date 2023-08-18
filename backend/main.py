from fastapi import FastAPI
from prisma import Prisma

app = FastAPI()
prisma = Prisma()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup():
        await prisma.connect()
        
        
@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()