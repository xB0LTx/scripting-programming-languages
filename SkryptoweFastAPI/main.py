from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class MyItem(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# Przykładowa baza danych
database: List[MyItem] = [
    MyItem(id=1, name="Item1", description="Description1", price=10.0),
    MyItem(id=2, name="Item2", description="Description2", price=20.0),
    MyItem(id=3, name="Item3", description="Description3", price=30.0)
]


# Zadanie 1: Endpointy GET
@app.get("/items", response_model=List[MyItem])
def get_all_items():
    return database


@app.get("/items/{item_id}", response_model=MyItem)
def get_item(item_id: int):
    item = next((item for item in database if item_id == item.id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# Zadanie 2: Endpoint POST
@app.post("/items", response_model=MyItem)
def create_item(item: MyItem):
    database.append(item)
    return item


# Zadanie 3: Endpoint PUT
@app.put("/items/{item_id}", response_model=MyItem)
def update_item(item_id: int, updated_item: MyItem):
    index = next((index for index, item in enumerate(database) if item_id == item.id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Item not found")

    database[index] = updated_item
    return updated_item


# Zadanie 4: Endpointy DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    database[:] = [item for item in database if item.id == 4]
    return {"message": "Item deleted"}


@app.delete("/items")
def delete_all_items():
    database.clear()
    return {"message": "All items deleted"}


# Zadanie 5: Automatyczna dokumentacja
# Swagger UI: http://127.0.0.1:8000/docs
# ReDoc: http://127.0.0.1:8000/redoc


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
