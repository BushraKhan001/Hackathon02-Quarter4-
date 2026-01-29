# Data Model: Todo CLI Core

## Overview
This document defines the data models for the Todo CLI Core feature.

## Todo Item Entity

### Fields
- **id** (integer): Unique identifier for the todo item
- **title** (string): The title or description of the todo item (required)
- **completed** (boolean): Status indicating if the todo is completed (default: false)
- **created_at** (datetime): Timestamp when the todo was created
- **updated_at** (datetime): Timestamp when the todo was last updated

### Relationships
- No direct relationships with other entities in this initial implementation

### Validation Rules
- Title cannot be empty or null
- ID must be unique within the system
- Completed status must be a boolean value
- created_at and updated_at must be valid datetime values

### State Transitions
- New todo: created_at set to current time, completed = false
- Update todo: updated_at updated to current time
- Complete todo: completed = true, updated_at updated
- Uncomplete todo: completed = false, updated_at updated

## Storage Schema

### JSON Structure
```json
{
  "todos": [
    {
      "id": 1,
      "title": "Sample todo item",
      "completed": false,
      "created_at": "2026-01-08T14:30:00Z",
      "updated_at": "2026-01-08T14:30:00Z"
    }
  ]
}
```

## Data Access Patterns
- Retrieve all todos
- Retrieve single todo by ID
- Create new todo
- Update existing todo
- Delete todo by ID
- Mark todo as completed/incomplete