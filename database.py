from motor.motor_asyncio import AsyncIOMotorClient

# Replace with your MongoDB connection string
MONGO_URL = "your_mongodb_connection_string"

client = AsyncIOMotorClient(MONGO_URL)
db = client.inventory_db  # database
collection = db.items     # collection
