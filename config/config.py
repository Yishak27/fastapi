import os
from dotenv import load_dotenv

load_dotenv()

class Setting:
    MONGO_URL:str = os.getenv("MONGO_URL","mongodb://localhost:27017/Fusm")

setting = Setting()