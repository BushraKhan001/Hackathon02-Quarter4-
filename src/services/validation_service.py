"""
Validation Service
Handles validation of todo data before any action is performed.
Delegates to the Todo Validator sub-agent as per constitution.
"""

from typing import Any
from src.models.todo_item import TodoItem


class ValidationService:
    """
    Service responsible for validating todo data before any action is performed.
    Follows the constitution by delegating validation to the Todo Validator sub-agent.
    """
    
    @staticmethod
    def validate_todo_title(title: str) -> bool:
        """
        Validate that the todo title is not empty.
        
        Args:
            title (str): The title to validate
            
        Returns:
            bool: True if valid, raises ValueError if invalid
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or null")
        return True
    
    @staticmethod
    def validate_todo_id_exists(todo_id: int, todos: list) -> bool:
        """
        Validate that a todo with the given ID exists.
        
        Args:
            todo_id (int): The ID to validate
            todos (list): List of existing todos to check against
            
        Returns:
            bool: True if valid, raises ValueError if invalid
        """
        if not any(todo.id == todo_id for todo in todos):
            raise ValueError(f"Todo with ID {todo_id} does not exist")
        return True
    
    @staticmethod
    def validate_completed_status(completed: Any) -> bool:
        """
        Validate that the completed status is a boolean.
        
        Args:
            completed (Any): The completed status to validate
            
        Returns:
            bool: True if valid, raises ValueError if invalid
        """
        if not isinstance(completed, bool):
            raise ValueError("Completed status must be a boolean value")
        return True
    
    @staticmethod
    def validate_todo_item(todo: TodoItem) -> bool:
        """
        Validate a complete TodoItem object.
        
        Args:
            todo (TodoItem): The TodoItem to validate
            
        Returns:
            bool: True if valid, raises ValueError if invalid
        """
        ValidationService.validate_todo_title(todo.title)
        ValidationService.validate_completed_status(todo.completed)
        return True