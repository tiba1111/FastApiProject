import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    address_postcode: str = os.getenv("ADDRESS_POSTCODE", "00000")

settings = Settings()
