"""
Simple test script to verify the todo CLI functionality
"""
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath('.'))

try:
    from src.models.todo_item import TodoItem
    print("✓ TodoItem class imported successfully")
    
    # Test creating a todo item
    todo = TodoItem(id=1, title="Test todo")
    print(f"✓ Todo created: {todo.title} (ID: {todo.id}, Completed: {todo.completed})")
    
    # Test marking as complete
    todo.mark_complete()
    print(f"✓ Todo marked complete: {todo.completed}")
    
    # Test updating title
    todo.update_title("Updated test todo")
    print(f"✓ Todo title updated: {todo.title}")
    
except Exception as e:
    print(f"✗ Error testing TodoItem: {e}")
    import traceback
    traceback.print_exc()

try:
    from src.lib.storage import Storage
    print("✓ Storage class imported successfully")
    
    # Test creating storage
    storage = Storage("test_todos.json")
    print("✓ Storage instance created")
    
except Exception as e:
    print(f"✗ Error testing Storage: {e}")
    import traceback
    traceback.print_exc()

try:
    from src.services.validation_service import ValidationService
    print("✓ ValidationService class imported successfully")
    
    # Test validation
    ValidationService.validate_todo_title("Valid title")
    print("✓ Title validation works")
    
except Exception as e:
    print(f"✗ Error testing ValidationService: {e}")
    import traceback
    traceback.print_exc()

try:
    from src.services.todo_service import TodoService
    print("✓ TodoService class imported successfully")
    
    # Test creating service
    service = TodoService()
    print("✓ TodoService instance created")
    
    # Test adding a todo
    new_todo = service.add_todo("Test service todo")
    print(f"✓ Todo added via service: {new_todo.title}")
    
    # Test listing todos
    todos = service.list_todos()
    print(f"✓ Todo list retrieved: {len(todos)} todos")
    
except Exception as e:
    print(f"✗ Error testing TodoService: {e}")
    import traceback
    traceback.print_exc()

print("\nAll tests completed!")