# Quickstart Guide: Todo CLI Core

## Overview
This guide provides instructions for getting started with the Todo CLI Core application.

## Prerequisites
- Python 3.11 or higher
- Command-line interface (Terminal on macOS/Linux, Command Prompt or PowerShell on Windows)

## Installation
1. Clone or download the Todo CLI Core application
2. Navigate to the application directory
3. No additional installation required - the application runs directly with Python

## Basic Usage

### View Help
```bash
python src/cli/todo_app.py --help
```

### Add a New Todo
```bash
python src/cli/todo_app.py add "Buy groceries"
```

### List All Todos
```bash
python src/cli/todo_app.py list
```

### Mark a Todo as Complete
```bash
python src/cli/todo_app.py complete 1
```

### Mark a Todo as Incomplete
```bash
python src/cli/todo_app.py incomplete 1
```

### Update a Todo
```bash
python src/cli/todo_app.py update 1 "Buy groceries - urgent"
```

### Delete a Todo
```bash
python src/cli/todo_app.py delete 1
```

## Interactive Menu
The application also includes an interactive menu system:
```bash
python src/reach_menu.py
```

## Example Workflow
1. Add a new todo: `python src/cli/todo_app.py add "Complete project proposal"`
2. View all todos: `python src/cli/todo_app.py list`
3. Mark as complete: `python src/cli/todo_app.py complete 1`
4. Update if needed: `python src/cli/todo_app.py update 1 "Completed project proposal"`
5. Delete when no longer needed: `python src/cli/todo_app.py delete 1`

## Data Storage
Todos are stored in a local file named `todos.json` in the current directory. The file is automatically created when the first todo is added.

## Troubleshooting
- If you get a "command not found" error, ensure you're running the command from the directory containing the source files
- If you encounter permission errors, ensure you have write access to the current directory
- For any validation errors, check that your todo titles are not empty