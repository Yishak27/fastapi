from motor.motor_asyncio import AsyncIOMotorClient
from config import setting

client = AsyncIOMotorClient(setting.MONGO_URL)
db = client[setting.MONGO_URL]

