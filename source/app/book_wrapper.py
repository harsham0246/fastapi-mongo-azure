import json_wrapper as json_ops


class BookOperations():

    def add_book_details(id:int, details: dict) -> bool:
        books = json_ops.load_books()
        if str(id) in books:
            raise KeyError(f"Book with ID {id} already exists.")
        json_ops.update_book("add", id=id, new_data=details)
        return True

    def update_book_details(id: int, details: dict) -> bool:
        json_ops.update_book("update", id=id, new_data=details)
        return True

    def delete_book_details(id: int) -> bool:
        json_ops.update_book("delete", id=id)
        return True

    def get_book_details(id: int):
        books = json_ops.load_books()
        if str(id) in books:
            return books[str(id)]
        raise KeyError(f"Book with ID {id} not found.")

    def get_books_list():
        books = json_ops.load_books()
        books_list = []
        for book_id, book_details in books.items():
            books_list.append(f"{book_id}: {book_details['name']}")
        return books_list
