import motor.motor_asyncio
from os import getenv

def get_collection():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        getenv("MONGO_URI"),
       
    )
    DB = "Scraper"

    bd = client[DB]["ChallengeBack"]
    yield bd



