# API Contract: Todo CLI Core

## Overview
This document specifies the API contract for the Todo CLI Core feature, defining the expected inputs, outputs, and behaviors for each command.

## Command Definitions

### Add Todo
**Command**: `add <title>`
- **Input**: Title string (non-empty)
- **Output**: Success message with new todo ID or error message
- **Behavior**: Creates a new todo with the provided title, sets completed to false, assigns unique ID, and saves to storage
- **Validation**: Title must not be empty
- **Example**: `todo_app.py add "Buy groceries"`

### List Todos
**Command**: `list`
- **Input**: None
- **Output**: Formatted list of all todos showing ID, title, and completion status
- **Behavior**: Retrieves all todos from storage and displays them in a readable format
- **Example**: `todo_app.py list`

### Complete Todo
**Command**: `complete <id>`
- **Input**: Valid todo ID (integer)
- **Output**: Success message or error message if ID not found
- **Behavior**: Updates the specified todo's completion status to true
- **Validation**: Todo with given ID must exist
- **Example**: `todo_app.py complete 1`

### Incomplete Todo
**Command**: `incomplete <id>`
- **Input**: Valid todo ID (integer)
- **Output**: Success message or error message if ID not found
- **Behavior**: Updates the specified todo's completion status to false
- **Validation**: Todo with given ID must exist
- **Example**: `todo_app.py incomplete 1`

### Update Todo
**Command**: `update <id> <new_title>`
- **Input**: Valid todo ID (integer) and new title string (non-empty)
- **Output**: Success message or error message if ID not found or title is empty
- **Behavior**: Updates the title of the specified todo
- **Validation**: Todo with given ID must exist, title must not be empty
- **Example**: `todo_app.py update 1 "Buy groceries - urgent"`

### Delete Todo
**Command**: `delete <id>`
- **Input**: Valid todo ID (integer)
- **Output**: Success message or error message if ID not found
- **Behavior**: Removes the specified todo from storage
- **Validation**: Todo with given ID must exist
- **Example**: `todo_app.py delete 1`

## Error Handling
- Invalid command: Display help message
- Missing arguments: Display specific error and usage hint
- Invalid ID: "Todo with ID <id> not found"
- Empty title: "Title cannot be empty"
- General error: Descriptive error message

## Exit Codes
- 0: Success
- 1: General error
- 2: Usage error (invalid arguments)
- 3: Resource not found (todo ID doesn't exist)