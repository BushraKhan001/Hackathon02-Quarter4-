"""
Data Persistence Layer
Handles saving and loading todo items to/from a local JSON file.
Following Safe and Predictable Behavior principle from the constitution.
"""

import json
import os
from typing import List, Dict, Any
from src.models.todo_item import TodoItem


class Storage:
    """
    Handles data persistence for todo items using a local JSON file.
    """
    
    def __init__(self, file_path: str = "todos.json"):
        """
        Initialize the storage with a file path.
        
        Args:
            file_path (str): Path to the JSON file for storing todos
        """
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Ensure the storage file exists, create it with empty todos if it doesn't."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({"todos": []}, f)
    
    def load_todos(self) -> List[TodoItem]:
        """
        Load all todo items from the storage file.
        
        Returns:
            List[TodoItem]: List of loaded TodoItem objects
        """
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                todos_data = data.get("todos", [])
                return [TodoItem.from_dict(todo_data) for todo_data in todos_data]
        except FileNotFoundError:
            # If file doesn't exist, return empty list
            return []
        except json.JSONDecodeError:
            # If file is corrupted, return empty list
            return []
    
    def save_todos(self, todos: List[TodoItem]):
        """
        Save all todo items to the storage file.
        
        Args:
            todos (List[TodoItem]): List of TodoItem objects to save
        """
        todos_data = [todo.to_dict() for todo in todos]
        data = {"todos": todos_data}
        
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_todo(self, todo: TodoItem):
        """
        Add a single todo item to the storage.
        
        Args:
            todo (TodoItem): TodoItem to add
        """
        todos = self.load_todos()
        todos.append(todo)
        self.save_todos(todos)
    
    def update_todo(self, todo: TodoItem):
        """
        Update an existing todo item in the storage.
        
        Args:
            todo (TodoItem): TodoItem with updated information
        """
        todos = self.load_todos()
        for i, existing_todo in enumerate(todos):
            if existing_todo.id == todo.id:
                todos[i] = todo
                break
        self.save_todos(todos)
    
    def delete_todo(self, todo_id: int):
        """
        Delete a todo item from the storage by ID.
        
        Args:
            todo_id (int): ID of the todo to delete
        """
        todos = self.load_todos()
        todos = [todo for todo in todos if todo.id != todo_id]
        self.save_todos(todos)  