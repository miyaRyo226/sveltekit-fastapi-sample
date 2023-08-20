from fastapi import FastAPI
from .prisma import prisma
from .routers import auth

app: FastAPI = FastAPI()
app.include_router(auth.router)

@app.on_event("startup")
async def startup() -> None:
 await prisma.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
 await prisma.disconnect()
