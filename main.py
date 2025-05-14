from fastapi import FastAPI, HTTPException
from models import Item
from database import collection
from bson import ObjectId

app = FastAPI()

# Helper to convert MongoDB ID to string
def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "category": item["category"],
        "price": item["price"],
        "in_stock": item["in_stock"],
    }

@app.post("/items/")
async def create_item(item: Item):
    new_item = await collection.insert_one(item.dict())
    created_item = await collection.find_one({"_id": new_item.inserted_id})
    return item_helper(created_item)

@app.get("/items/")
async def get_all_items():
    items = []
    async for item in collection.find():
        items.append(item_helper(item))
    return items

@app.get("/items/{item_id}")
async def get_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return item_helper(item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    result = await collection.update_one(
        {"_id": ObjectId(item_id)}, {"$set": item.dict()}
    )
    if result.modified_count == 1:
        updated_item = await collection.find_one({"_id": ObjectId(item_id)})
        return item_helper(updated_item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
@app.get("/")
async def root():
    return {"Welcome to the Inventory Manager API!"}

