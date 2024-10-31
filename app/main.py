from fastapi import FastAPI, HTTPException
import crud
from pydantic import BaseModel

app = FastAPI()


class CreateItemRequest(BaseModel):
    name: str
    description: str
    price: float
    tax: float


class UpdateItemRequest(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float | None = None


@app.get("/items/{item_id}", response_model=dict)
async def get_item(item_id: int):
    item = crud.get_item(item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "tax": item.tax}


@app.get("/items", response_model=list)
async def get_items(skip: int = 0, limit: int = 10):
    items = crud.get_items(skip=skip, limit=limit)
    return [{"id": item.id,
             "name": item.name,
             "description": item.description,
             "price": item.price,
             "tax": item.tax} for item in items]


@app.post("/items", response_model=dict)
async def create_item(item_request: CreateItemRequest):
    item = crud.create_item(
        name=item_request.name,
        description=item_request.description,
        price=item_request.price,
        tax=item_request.tax)
    return {"id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "tax": item.tax}


@app.put("/items/{item_id}", response_model=dict)
async def update_item(item_id: int, item_request: UpdateItemRequest):
    item = crud.update_item(
        item_id=item_id,
        name=item_request.name,
        description=item_request.description,
        price=item_request.price,
        tax=item_request.tax)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "tax": item.tax}


@app.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    item = crud.delete_item(item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "tax": item.tax}

