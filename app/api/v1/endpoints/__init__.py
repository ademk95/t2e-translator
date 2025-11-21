from fastapi import APIRouter
from . import my_translate

router = APIRouter()

router.include_router(my_translate.router, prefix="/my-translate", tags=["my-translate"])