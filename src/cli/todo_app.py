"""
Todo CLI Application
Main entry point for the todo CLI application.
Follows Instruction-Based Agent Architecture from the constitution.
"""

import argparse
import sys
from src.services.todo_service import TodoService
from src.lib.storage import Storage


def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Todo CLI - A simple command-line todo manager"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new todo')
    add_parser.add_argument('title', nargs='+', help='Title of the todo')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all todos')
    
    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark a todo as complete')
    complete_parser.add_argument('id', type=int, help='ID of the todo to complete')
    
    # Incomplete command
    incomplete_parser = subparsers.add_parser('incomplete', help='Mark a todo as incomplete')
    incomplete_parser.add_argument('id', type=int, help='ID of the todo to mark as incomplete')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update a todo title')
    update_parser.add_argument('id', type=int, help='ID of the todo to update')
    update_parser.add_argument('title', nargs='+', help='New title for the todo')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a todo')
    delete_parser.add_argument('id', type=int, help='ID of the todo to delete')
    
    return parser


def main():
    """Main entry point for the todo CLI application."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Initialize services
    storage = Storage()
    todo_service = TodoService(storage)
    
    # Handle commands
    if args.command == 'add':
        title = ' '.join(args.title)
        try:
            new_todo = todo_service.add_todo(title)
            print(f"Added todo with ID {new_todo.id}: {new_todo.title}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    elif args.command == 'list':
        todos = todo_service.list_todos()
        if not todos:
            print("No todos found.")
        else:
            print(f"Found {len(todos)} todo(s):")
            for todo in todos:
                status = "✓" if todo.completed else "○"
                print(f"  [{status}] {todo.id}: {todo.title}")
    
    elif args.command == 'complete':
        try:
            todo = todo_service.complete_todo(args.id)
            print(f"Marked todo {todo.id} as complete: {todo.title}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    elif args.command == 'incomplete':
        try:
            todo = todo_service.incomplete_todo(args.id)
            print(f"Marked todo {todo.id} as incomplete: {todo.title}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    elif args.command == 'update':
        title = ' '.join(args.title)
        try:
            updated_todo = todo_service.update_todo(args.id, title)
            print(f"Updated todo {updated_todo.id}: {updated_todo.title}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    elif args.command == 'delete':
        try:
            # Get the todo before deletion to show what was deleted
            todo = todo_service.get_todo_by_id(args.id)
            todo_service.delete_todo(args.id)
            print(f"Deleted todo {todo.id}: {todo.title}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    elif args.command is None:
        parser.print_help()
    
    else:
        print(f"Unknown command: {args.command}")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()