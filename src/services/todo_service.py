"""
Todo Service
Contains the business logic for todo operations.
Follows Clear Hierarchy and Responsibility principle from the constitution.
"""

from typing import List
from src.models.todo_item import TodoItem
from src.lib.storage import Storage
from src.services.validation_service import ValidationService


class TodoService:
    """
    Service responsible for business logic related to todo operations.
    """

    def __init__(self, storage: Storage = None):
        """
        Initialize the TodoService with a storage instance.

        Args:
            storage (Storage): Storage instance for data persistence
        """
        self.storage = storage or Storage()

    def add_todo(self, title: str) -> TodoItem:
        """
        Add a new todo with the given title.

        Args:
            title (str): The title of the new todo

        Returns:
            TodoItem: The newly created TodoItem
        """
        # Validate the title
        ValidationService.validate_todo_title(title)

        # Load existing todos to determine the next ID
        existing_todos = self.storage.load_todos()

        # Determine the next ID (highest existing ID + 1, or 1 if no todos exist)
        next_id = 1
        if existing_todos:
            next_id = max(todo.id for todo in existing_todos) + 1

        # Create the new todo
        new_todo = TodoItem(id=next_id, title=title)

        # Save the new todo
        self.storage.add_todo(new_todo)

        return new_todo

    def list_todos(self) -> List[TodoItem]:
        """
        List all todos.

        Returns:
            List[TodoItem]: List of all TodoItem objects
        """
        return self.storage.load_todos()

    def get_todo_by_id(self, todo_id: int) -> TodoItem:
        """
        Get a specific todo by its ID.

        Args:
            todo_id (int): The ID of the todo to retrieve

        Returns:
            TodoItem: The requested TodoItem

        Raises:
            ValueError: If no todo with the given ID exists
        """
        todos = self.storage.load_todos()
        ValidationService.validate_todo_id_exists(todo_id, todos)

        for todo in todos:
            if todo.id == todo_id:
                return todo

        # This should not happen if validation passes, but included for safety
        raise ValueError(f"Todo with ID {todo_id} does not exist")

    def update_todo(self, todo_id: int, new_title: str) -> TodoItem:
        """
        Update the title of an existing todo.

        Args:
            todo_id (int): The ID of the todo to update
            new_title (str): The new title for the todo

        Returns:
            TodoItem: The updated TodoItem
        """
        # Load existing todos to validate the ID
        todos = self.storage.load_todos()
        ValidationService.validate_todo_id_exists(todo_id, todos)

        # Validate the new title
        ValidationService.validate_todo_title(new_title)

        # Find and update the todo
        for todo in todos:
            if todo.id == todo_id:
                todo.update_title(new_title)
                self.storage.update_todo(todo)
                return todo

        # This should not happen if validation passes, but included for safety
        raise ValueError(f"Todo with ID {todo_id} does not exist")

    def complete_todo(self, todo_id: int) -> TodoItem:
        """
        Mark a todo as completed.

        Args:
            todo_id (int): The ID of the todo to mark as completed

        Returns:
            TodoItem: The updated TodoItem
        """
        # Load existing todos to validate the ID
        todos = self.storage.load_todos()
        ValidationService.validate_todo_id_exists(todo_id, todos)

        # Find and update the todo
        for todo in todos:
            if todo.id == todo_id:
                todo.mark_complete()
                self.storage.update_todo(todo)
                return todo

        # This should not happen if validation passes, but included for safety
        raise ValueError(f"Todo with ID {todo_id} does not exist")

    def incomplete_todo(self, todo_id: int) -> TodoItem:
        """
        Mark a todo as incomplete.

        Args:
            todo_id (int): The ID of the todo to mark as incomplete

        Returns:
            TodoItem: The updated TodoItem
        """
        # Load existing todos to validate the ID
        todos = self.storage.load_todos()
        ValidationService.validate_todo_id_exists(todo_id, todos)

        # Find and update the todo
        for todo in todos:
            if todo.id == todo_id:
                todo.mark_incomplete()
                self.storage.update_todo(todo)
                return todo

        # This should not happen if validation passes, but included for safety
        raise ValueError(f"Todo with ID {todo_id} does not exist")

    def delete_todo(self, todo_id: int):
        """
        Delete a todo by its ID.

        Args:
            todo_id (int): The ID of the todo to delete
        """
        # Load existing todos to validate the ID
        todos = self.storage.load_todos()
        ValidationService.validate_todo_id_exists(todo_id, todos)

        # Delete the todo
        self.storage.delete_todo(todo_id)