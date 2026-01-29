# Test basic functionality of the implemented components
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath('.'))

# Test the TodoItem model
from src.models.todo_item import TodoItem

# Create a new todo item
todo = TodoItem(id=1, title="Test todo item")
print(f"Created todo: {todo.title} (ID: {todo.id})")

# Test marking as complete
todo.mark_complete()
print(f"Marked as complete: {todo.completed}")

# Test updating the title
todo.update_title("Updated test todo item")
print(f"Updated title: {todo.title}")

# Test the storage layer
from src.lib.storage import Storage

# Create storage instance
storage = Storage("test_todos.json")
print("Storage initialized")

# Add the todo to storage
storage.add_todo(todo)
print("Todo added to storage")

# Load todos from storage
loaded_todos = storage.load_todos()
print(f"Loaded {len(loaded_todos)} todos from storage")

# Test the validation service
from src.services.validation_service import ValidationService

try:
    ValidationService.validate_todo_title("Valid title")
    print("Title validation passed")
except ValueError as e:
    print(f"Title validation failed: {e}")

# Test the todo service
from src.services.todo_service import TodoService

service = TodoService(storage)
print("Todo service initialized")

# Add another todo via service
new_todo = service.add_todo("Second test todo")
print(f"Added via service: {new_todo.title}")

# List all todos
all_todos = service.list_todos()
print(f"Total todos via service: {len(all_todos)}")

print("All tests completed successfully!")