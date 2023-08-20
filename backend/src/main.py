from fastapi import FastAPI
from prisma import Prisma

app = FastAPI()
prisma = Prisma()


@app.on_event("startup")
async def startup() -> None:
 await prisma.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
 await prisma.disconnect()
