# FastAPI Starter Code
# Run with: uvicorn main:app --reload

from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST Assignment")

class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

_items: List[Item] = []
_next_id: int = 1

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items", response_model=List[Item])
def list_items(skip: int = 0, limit: int = 100):
    return _items[skip: skip + limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in _items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items", status_code=201, response_model=Item)
def create_item(payload: ItemCreate):
    global _next_id
    item = Item(id=_next_id, **payload.model_dump())
    _items.append(item)
    _next_id += 1
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate):
    for idx, item in enumerate(_items):
        if item.id == item_id:
            updated = Item(id=item_id, **payload.model_dump())
            _items[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, item in enumerate(_items):
        if item.id == item_id:
            _items.pop(idx)
            return {"deleted": item_id}
    raise HTTPException(status_code=404, detail="Item not found")
