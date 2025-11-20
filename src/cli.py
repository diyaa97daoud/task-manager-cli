"""Command-line interface for the Task Manager application."""

import logging
import sys
from pathlib import Path
from typing import Optional
import click
from colorama import init, Fore, Style
from src.task_manager import TaskManager, TaskPriority, TaskStatus

# Initialize colorama for Windows support
init(autoreset=True)

# Configure logging
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "task_manager.log"

# Configure root logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)

# Set third-party loggers to WARNING to reduce noise
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def print_success(message: str) -> None:
    """Print success message in green."""
    click.echo(f"{Fore.GREEN}✓ {message}{Style.RESET_ALL}")


def print_error(message: str) -> None:
    """Print error message in red."""
    click.echo(f"{Fore.RED}✗ {message}{Style.RESET_ALL}")


def print_warning(message: str) -> None:
    """Print warning message in yellow."""
    click.echo(f"{Fore.YELLOW}⚠ {message}{Style.RESET_ALL}")


def print_info(message: str) -> None:
    """Print info message in blue."""
    click.echo(f"{Fore.BLUE}ℹ {message}{Style.RESET_ALL}")


def get_priority_color(priority: str) -> str:
    """Get color for priority level."""
    colors = {
        TaskPriority.LOW: Fore.GREEN,
        TaskPriority.MEDIUM: Fore.YELLOW,
        TaskPriority.HIGH: Fore.MAGENTA,
        TaskPriority.CRITICAL: Fore.RED,
    }
    return colors.get(priority, Fore.WHITE)  # type: ignore[no-any-return]


def get_status_color(status: str) -> str:
    """Get color for status."""
    colors = {
        TaskStatus.TODO: Fore.CYAN,
        TaskStatus.IN_PROGRESS: Fore.YELLOW,
        TaskStatus.COMPLETED: Fore.GREEN,
        TaskStatus.CANCELLED: Fore.RED,
    }
    return colors.get(status, Fore.WHITE)  # type: ignore[no-any-return]


@click.group()
@click.version_option(version="1.0.0")
def cli() -> None:
    """Task Manager CLI - Manage your tasks efficiently."""
    logger.info("Task Manager CLI started")


@cli.command()
@click.argument("title")
@click.option("--description", "-d", default="", help="Task description")
@click.option(
    "--priority",
    "-p",
    type=click.Choice(
        [TaskPriority.LOW, TaskPriority.MEDIUM, TaskPriority.HIGH, TaskPriority.CRITICAL]
    ),
    default=TaskPriority.MEDIUM,
    help="Task priority",
)
@click.option("--due-date", help="Due date (ISO format: YYYY-MM-DD)")
def add(title: str, description: str, priority: str, due_date: Optional[str]) -> None:
    """Add a new task."""
    logger.info("Adding new task: title='%s', priority=%s", title, priority)

    try:
        manager = TaskManager()
        task = manager.add_task(
            title=title, description=description, priority=priority, due_date=due_date
        )
        print_success(f"Task added with ID: {task.task_id}")
        logger.info("Task successfully added: id=%d", task.task_id)
    except ValueError as e:
        print_error(f"Invalid input: {e}")
        logger.error("Failed to add task: %s", e)
        sys.exit(1)
    except Exception as e:  # pylint: disable=broad-exception-caught
        print_error(f"Failed to add task: {e}")
        logger.critical("Unexpected error adding task: %s", e, exc_info=True)
        sys.exit(1)


@cli.command(name="list")
@click.option("--status", "-s", help="Filter by status")
@click.option("--priority", "-p", help="Filter by priority")
@click.option("--overdue", is_flag=True, help="Show only overdue tasks")
def list_tasks(status: Optional[str], priority: Optional[str], overdue: bool) -> None:
    """List all tasks."""
    logger.info("Listing tasks: status=%s, priority=%s, overdue=%s", status, priority, overdue)

    try:
        manager = TaskManager()

        if overdue:
            tasks = manager.get_overdue_tasks()
            if not tasks:
                print_info("No overdue tasks!")
                return
        else:
            tasks = manager.list_tasks(status=status, priority=priority)

        if not tasks:
            print_info("No tasks found.")
            logger.info("No tasks matched the criteria")
            return

        click.echo(
            f"\n{Fore.CYAN}{'ID':<5} {'Title':<30} {'Priority':<10} "
            f"{'Status':<15} {'Due Date':<12}{Style.RESET_ALL}"
        )
        click.echo("=" * 80)

        for task in tasks:
            priority_color = get_priority_color(task.priority)
            status_color = get_status_color(task.status)
            due_str = task.due_date[:10] if task.due_date else "N/A"

            overdue_marker = " [OVERDUE]" if task.is_overdue() else ""

            click.echo(
                f"{task.task_id:<5} {task.title:<30} "
                f"{priority_color}{task.priority:<10}{Style.RESET_ALL} "
                f"{status_color}{task.status:<15}{Style.RESET_ALL} "
                f"{due_str:<12}"
                f"{Fore.RED if task.is_overdue() else ''}"
                f"{overdue_marker}{Style.RESET_ALL}"
            )

        logger.info("Listed %d tasks", len(tasks))

    except Exception as e:  # pylint: disable=broad-exception-caught
        print_error(f"Failed to list tasks: {e}")
        logger.critical("Error listing tasks: %s", e, exc_info=True)
        sys.exit(1)


@cli.command()
@click.argument("task_id", type=int)
def show(task_id: int) -> None:
    """Show detailed information about a task."""
    logger.debug("Showing details for task: id=%d", task_id)

    try:
        manager = TaskManager()
        task = manager.get_task(task_id)

        if not task:
            print_error(f"Task {task_id} not found.")
            return

        click.echo(f"\n{Fore.CYAN}Task Details:{Style.RESET_ALL}")
        click.echo(f"ID:          {task.task_id}")
        click.echo(f"Title:       {task.title}")
        click.echo(f"Description: {task.description or 'N/A'}")
        click.echo(
            f"Priority:    {get_priority_color(task.priority)}{task.priority}{Style.RESET_ALL}"
        )
        click.echo(f"Status:      {get_status_color(task.status)}{task.status}{Style.RESET_ALL}")
        click.echo(f"Due Date:    {task.due_date or 'N/A'}")
        click.echo(f"Created:     {task.created_at}")
        click.echo(f"Updated:     {task.updated_at}")

        if task.is_overdue():
            print_warning("This task is OVERDUE!")

    except Exception as e:  # pylint: disable=broad-exception-caught
        print_error(f"Failed to show task: {e}")
        logger.error("Error showing task %d: %s", task_id, e)
        sys.exit(1)


@cli.command()
@click.argument("task_id", type=int)
@click.option("--status", "-s", help="New status")
@click.option("--priority", "-p", help="New priority")
@click.option("--title", "-t", help="New title")
@click.option("--description", "-d", help="New description")
@click.option("--due-date", help="New due date")
def update(  # pylint: disable=too-many-arguments
    task_id: int,
    status: Optional[str],
    priority: Optional[str],
    title: Optional[str],
    description: Optional[str],
    due_date: Optional[str],
) -> None:
    """Update an existing task."""
    logger.info("Updating task: id=%d", task_id)

    try:
        manager = TaskManager()
        success = manager.update_task(
            task_id=task_id,
            title=title,
            description=description,
            priority=priority,
            status=status,
            due_date=due_date,
        )

        if success:
            print_success(f"Task {task_id} updated successfully.")
        else:
            print_error(f"Task {task_id} not found.")

    except Exception as e:  # pylint: disable=broad-exception-caught
        print_error(f"Failed to update task: {e}")
        logger.error("Error updating task %d: %s", task_id, e)
        sys.exit(1)


@cli.command()
@click.argument("task_id", type=int)
@click.confirmation_option(prompt="Are you sure you want to delete this task?")
def delete(task_id: int) -> None:
    """Delete a task."""
    logger.info("Deleting task: id=%d", task_id)

    try:
        manager = TaskManager()
        success = manager.delete_task(task_id)

        if success:
            print_success(f"Task {task_id} deleted successfully.")
        else:
            print_error(f"Task {task_id} not found.")

    except Exception as e:  # pylint: disable=broad-exception-caught
        print_error(f"Failed to delete task: {e}")
        logger.error("Error deleting task %d: %s", task_id, e)
        sys.exit(1)


@cli.command()
@click.argument("task_id", type=int)
def complete(task_id: int) -> None:
    """Mark a task as completed."""
    logger.info("Marking task as completed: id=%d", task_id)

    try:
        manager = TaskManager()
        success = manager.update_task(task_id=task_id, status=TaskStatus.COMPLETED)

        if success:
            print_success(f"Task {task_id} marked as completed! 🎉")
        else:
            print_error(f"Task {task_id} not found.")

    except Exception as e:  # pylint: disable=broad-exception-caught
        print_error(f"Failed to complete task: {e}")
        logger.error("Error completing task %d: %s", task_id, e)
        sys.exit(1)


if __name__ == "__main__":
    cli()
