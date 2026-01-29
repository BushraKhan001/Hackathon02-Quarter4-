"""
Todo Item Model
Represents a single todo item with its properties and behaviors.
Following Specification-First Design principle from the constitution.
"""

from datetime import datetime
from typing import Dict, Any


class TodoItem:
    """
    Represents a todo item with id, title, completion status, and timestamps.
    """

    def __init__(self, id: int, title: str, completed: bool = False):
        """
        Initialize a TodoItem.

        Args:
            id (int): Unique identifier for the todo item
            title (str): The title or description of the todo item (required)
            completed (bool): Status indicating if the todo is completed (default: False)
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or null")

        self.id = id
        self.title = title.strip()
        self.completed = completed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def mark_complete(self):
        """Mark the todo as completed and update the timestamp."""
        self.completed = True
        self.updated_at = datetime.now()

    def mark_incomplete(self):
        """Mark the todo as incomplete and update the timestamp."""
        self.completed = False
        self.updated_at = datetime.now()

    def update_title(self, new_title: str):
        """Update the title and update the timestamp."""
        if not new_title or not new_title.strip():
            raise ValueError("Title cannot be empty or null")

        self.title = new_title.strip()
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the TodoItem to a dictionary representation.

        Returns:
            Dict[str, Any]: Dictionary representation of the TodoItem
        """
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TodoItem':
        """
        Create a TodoItem from a dictionary representation.

        Args:
            data (Dict[str, Any]): Dictionary representation of a TodoItem

        Returns:
            TodoItem: New TodoItem instance
        """
        from datetime import datetime

        item = cls(
            id=data["id"],
            title=data["title"],
            completed=data.get("completed", False)
        )
        item.created_at = datetime.fromisoformat(data["created_at"])
        item.updated_at = datetime.fromisoformat(data["updated_at"])

        return item