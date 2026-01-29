# Todo Specification

## Todo Structure
- id: number (unique)
- title: string (required)
- completed: boolean (default: false)

## Allowed Actions
- Create todo
- Update todo
- Delete todo
- List todos

## Rules
- Title must not be empty
- ID must exist for update or delete
- Deletion requires confirmation