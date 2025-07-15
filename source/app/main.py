import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Book(BaseModel):
    author: str
    description: str
    price: int
    available: bool
    rating: int
    gener: str


@app.post("/items/")
def create_item(book_details: Book):
    create_book_details()
    return {"message": "Successfully created book"}


@app.put("/items/{item_id}"
def update_item(item_id: int, item: Book):
    update_book_details()
    return {"message": "Updated book details"}


@app.get("items/{item_id}")
def get_item(item_id: int):
    book_details = get_book_details()
    return {"Book Details": book_details}


@app.delete("items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Successfully deleted book record"}


@app.get("/")
def list_items():
    books_list = get_books_list()
    return {"books": books_list}


@app.
if __name__ == "__main__":
    uvicorn.run(app)
