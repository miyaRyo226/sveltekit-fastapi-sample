from fastapi import APIRouter

router = APIRouter(prefix="/auth",tags=["auth"])

@router.get("/")
async def auth():
    pass
