import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI

from book_wrapper import BookOperations as book_ops

app = FastAPI()


class Book(BaseModel):
    # author: str
    # description: str
    # price: int
    # available: bool
    # rating: int
    # gener: str
    id: int
    name: str


@app.post("/items/")
def create_item(book_details: Book):
    id = book_details.id
    details = {"name": book_details.name}
    book_ops.add_book_details(id, details)
    return {"message": "Successfully created book"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Book):
    try:
        book_ops.update_book_details(item_id, item)
        return {"message": "Updated book details"}
    except KeyError as e:
        return {"error": str(e)}, 404


@app.get("/items/{item_id}")
def get_item(item_id: int):
    try:
        book_details = book_ops.get_book_details(item_id)
        return {"Book Details": book_details}
    except KeyError as e:
        return {"error": str(e)}, 404


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    try:
        book_ops.delete_book_details(item_id)
        return {"message": "Successfully deleted book record"}
    except KeyError as e:
        return {"error": str(e)}, 404


@app.get("/")
def list_items():
    books_list = book_ops.get_books_list()
    return {"books": books_list}


if __name__ == "__main__":
    uvicorn.run(app)
