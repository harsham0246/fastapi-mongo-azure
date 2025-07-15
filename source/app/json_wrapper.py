import os, json

FILE_PATH = os.path.abspath("books.json")


def file_exist(func):
    def wrapper(*args, **kwargs):
        if not os.path.exists(FILE_PATH):
            raise FileNotFoundError(f"File not found: {FILE_PATH}")
        return func(*args, **kwargs)
    return wrapper


@file_exist
def load_books() -> dict:
    """
    Load a JSON file and return its content.
    
    :return: Parsed JSON content as a Python dictionary.
    :raises json.JSONDecodeError: If the file is not valid JSON.
    """
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


@file_exist
def save_books(data) -> None:
    """
    Save data to a JSON file.
    
    :param data: Data to be saved, should be serializable to JSON.
    :raises IOError: If there is an error writing to the file.
    """
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def update_book(action, id: int=None, new_data: dict=None) -> None:
    """
    Append new data to a JSON file.
    
    :param new_data: Data to be appended, should be serializable to JSON.
    :raises ValueError: If the file content is not a list to append new items.
    """
    data = load_books()

    if not isinstance(data, dict):
        raise ValueError("Data must be a dict to append new items.")
    id = str(id)
    if action == "add":
        data[id] = new_data
        save_books(data)
        return
    
    if id not in data:
        raise KeyError(f"ID {id} not found in data.")
    
    if action == "update":
        data[id].update(new_data)
    elif action == "delete":
        data.pop(id)
        
    save_books(data)
