from fastapi import FastAPI,Query
from prisma import Prisma
import uvicorn

app = FastAPI()
prisma = Prisma()

@app.on_event("startup")
async def startup():
        await prisma.connect()
        
        
@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()