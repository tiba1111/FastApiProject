from fastapi import FastAPI

from config import settings
from routes import router

app = FastAPI(
    title="Address API",
    description="Returns address info with postcode from environment variable",
    version="1.0.0"
)



app.include_router(router)

