from contextlib import asynccontextmanager
import logging
from api.v1.endpoints import router as api_router
from fastapi import FastAPI
import uvicorn
from core.config import Settings
from fastapi.middleware.cors import CORSMiddleware

settings = Settings()
logger = logging.getLogger(settings.logger_name)
logger.setLevel(settings.log_level)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("API is firing up!")           
    yield
    logger.info("API is shutting down....")

app = FastAPI(lifespan=lifespan)

# origins = [
#     "http://localhost:4200",
#     "http://127.0.0.1:4200",
#     "http://172.24.96.247:4200",
#     "http://translateui.local.com"
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
     allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)

if __name__ == '__main__':
    uvicorn.run(app, port=8000)