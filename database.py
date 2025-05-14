from motor.motor_asyncio import AsyncIOMotorClient

# Replace with your MongoDB connection string
MONGO_URL = "mongodb+srv://saranyapentapati16:aradhy@2516@cluster0.02n8dyi.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"
client = AsyncIOMotorClient(MONGO_URL)
db = client.inventory_db  # database
collection = db.items     # collection
