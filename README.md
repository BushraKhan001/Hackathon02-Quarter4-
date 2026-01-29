# Todo CLI Core

A command-line interface application for managing todo items, built with Python.

## Features

- Add new todo items
- List all todo items
- Mark todos as complete/incomplete
- Update todo titles
- Delete todo items
- Interactive menu system
- JSON-based data persistence

## Prerequisites

- Python 3.11 or higher

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. No additional installation required

## Usage

### Command Line Interface

```bash
# Add a new todo
python src/cli/todo_app.py add "Buy groceries"

# List all todos
python src/cli/todo_app.py list

# Mark a todo as complete
python src/cli/todo_app.py complete 1

# Mark a todo as incomplete
python src/cli/todo_app.py incomplete 1

# Update a todo
python src/cli/todo_app.py update 1 "Buy groceries - urgent"

# Delete a todo
python src/cli/todo_app.py delete 1

# Show help
python src/cli/todo_app.py --help
```

### Interactive Menu

```bash
# Launch the interactive menu
python src/reach_menu.py
```

## Project Structure

```
src/
├── cli/
│   └── todo_app.py      # Main CLI application entry point
├── models/
│   └── todo_item.py     # Todo item data model
├── services/
│   ├── todo_service.py  # Business logic for todo operations
│   └── validation_service.py # Validation service (delegates to sub-agent)
└── lib/
    └── storage.py       # Data persistence layer
├── reach_menu.py        # Interactive menu system
```

## Architecture

This application follows the specification-driven, instruction-based agent architecture:

- **Specification-First Design**: All features fully specified before implementation
- **Instruction-Based Agent Architecture**: Agents defined by markdown instruction files
- **Spec-Driven Development**: Implementation follows specification exactly
- **Clear Hierarchy and Responsibility**: Proper agent responsibilities defined
- **Safe and Predictable Behavior**: Operations are safe and predictable
- **Human-Readable Instructions**: Components defined with clear documentation

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.