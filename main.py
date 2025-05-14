from fastapi import FastAPI, HTTPException
from uuid import uuid4
from models import Item
from database import collection
from couchbase.exceptions import DocumentNotFoundException

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_id = str(uuid4())
    collection.insert(item_id, item.dict())
    return {"id": item_id, **item.dict()}

@app.get("/items/")
async def read_items():
    # You'd normally query all items from the DB
    return {"message": "List of items - needs implementation"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    try:
        result = collection.get(item_id)
        return result.content_as[dict]
    except DocumentNotFoundException:
        raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    collection.replace(item_id, item.dict())
    return {"id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    collection.remove(item_id)
    return {"message": "Item deleted"}
