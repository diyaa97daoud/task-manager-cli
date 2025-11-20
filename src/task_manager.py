"""Task Manager - Core business logic for managing tasks."""

import logging
import json
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
from dateutil import parser as date_parser

# Configure logger for this module
logger = logging.getLogger(__name__)


class TaskPriority:
    """Task priority levels."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class TaskStatus:
    """Task status types."""

    TODO = "todo"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Task:
    """Represents a single task with metadata."""

    def __init__(
        self,
        title: str,
        description: str = "",
        priority: str = TaskPriority.MEDIUM,
        status: str = TaskStatus.TODO,
        due_date: Optional[str] = None,
        task_id: Optional[int] = None,
    ):
        """Initialize a task.

        Args:
            title: Task title
            description: Detailed task description
            priority: Task priority level
            status: Current task status
            due_date: Due date in ISO format
            task_id: Unique task identifier
        """
        if not title or not title.strip():
            logger.error("Attempted to create task with empty title")
            raise ValueError("Task title cannot be empty")

        self.title = title.strip()
        self.description = description.strip()
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.task_id = task_id
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

        logger.debug(
            "Task created: id=%s, title='%s', priority=%s",
            self.task_id,
            self.title,
            self.priority,
        )

    def to_dict(self) -> Dict:
        """Convert task to dictionary representation."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "due_date": self.due_date,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Task":
        """Create a task from dictionary representation."""
        task = cls(
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority", TaskPriority.MEDIUM),
            status=data.get("status", TaskStatus.TODO),
            due_date=data.get("due_date"),
            task_id=data.get("task_id"),
        )
        task.created_at = data.get("created_at", task.created_at)
        task.updated_at = data.get("updated_at", task.updated_at)
        return task

    def is_overdue(self) -> bool:
        """Check if task is overdue.

        Returns:
            True if task has a due date and it's in the past, False otherwise
        """
        if not self.due_date:
            logger.debug("Task %s has no due date", self.task_id)
            return False

        try:
            due = date_parser.parse(self.due_date)
            is_overdue = due < datetime.now() and self.status != TaskStatus.COMPLETED
            if is_overdue:
                logger.warning(
                    "Task %s ('%s') is overdue! Due: %s",
                    self.task_id,
                    self.title,
                    self.due_date,
                )
            return is_overdue
        except (ValueError, TypeError) as e:
            logger.error("Invalid due date format for task %s: %s", self.task_id, e)
            return False


class TaskManager:
    """Manages a collection of tasks with persistence."""

    def __init__(self, storage_path: str = "tasks.json"):
        """Initialize the task manager.

        Args:
            storage_path: Path to JSON file for task persistence
        """
        self.storage_path = Path(storage_path)
        self.tasks: List[Task] = []
        self.next_id = 1

        logger.info("TaskManager initialized with storage: %s", self.storage_path)
        self._load_tasks()

    def _load_tasks(self) -> None:
        """Load tasks from storage file."""
        if not self.storage_path.exists():
            logger.info("Storage file does not exist, starting with empty task list")
            return

        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data["tasks"]]
                self.next_id = data.get("next_id", 1)
                logger.info("Loaded %d tasks from storage", len(self.tasks))
        except json.JSONDecodeError as e:
            logger.error("Failed to parse JSON from %s: %s", self.storage_path, e)
            raise
        except Exception as e:
            logger.critical("Unexpected error loading tasks from %s: %s", self.storage_path, e)
            raise

    def _save_tasks(self) -> None:
        """Save tasks to storage file."""
        try:
            data = {
                "tasks": [task.to_dict() for task in self.tasks],
                "next_id": self.next_id,
            }
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.debug("Saved %d tasks to storage", len(self.tasks))
        except IOError as e:
            logger.critical("Failed to write to %s: %s", self.storage_path, e)
            raise

    def add_task(
        self,
        title: str,
        description: str = "",
        priority: str = TaskPriority.MEDIUM,
        due_date: Optional[str] = None,
    ) -> Task:
        """Add a new task.

        Args:
            title: Task title
            description: Task description
            priority: Task priority level
            due_date: Due date in ISO format

        Returns:
            The newly created task
        """
        task = Task(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            task_id=self.next_id,
        )
        self.tasks.append(task)
        self.next_id += 1
        self._save_tasks()

        logger.info("Task added: id=%d, title='%s'", task.task_id, task.title)
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID.

        Args:
            task_id: The task ID to search for

        Returns:
            The task if found, None otherwise
        """
        for task in self.tasks:
            if task.task_id == task_id:
                logger.debug("Task found: id=%d", task_id)
                return task

        logger.warning("Task not found: id=%d", task_id)
        return None

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[str] = None,
        status: Optional[str] = None,
        due_date: Optional[str] = None,
    ) -> bool:
        """Update an existing task.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)
            priority: New priority (optional)
            status: New status (optional)
            due_date: New due date (optional)

        Returns:
            True if task was updated, False if not found
        """
        task = self.get_task(task_id)
        if not task:
            logger.error("Cannot update task %d: task not found", task_id)
            return False

        if title is not None:
            task.title = title.strip()
        if description is not None:
            task.description = description.strip()
        if priority is not None:
            task.priority = priority
        if status is not None:
            old_status = task.status
            task.status = status
            logger.info("Task %d status changed: %s -> %s", task_id, old_status, status)
        if due_date is not None:
            task.due_date = due_date

        task.updated_at = datetime.now().isoformat()
        self._save_tasks()

        logger.info("Task updated: id=%d", task_id)
        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if task was deleted, False if not found
        """
        task = self.get_task(task_id)
        if not task:
            logger.error("Cannot delete task %d: task not found", task_id)
            return False

        self.tasks.remove(task)
        self._save_tasks()

        logger.info("Task deleted: id=%d, title='%s'", task_id, task.title)
        return True

    def list_tasks(
        self, status: Optional[str] = None, priority: Optional[str] = None
    ) -> List[Task]:
        """List tasks with optional filtering.

        Args:
            status: Filter by status (optional)
            priority: Filter by priority (optional)

        Returns:
            List of tasks matching the filters
        """
        filtered_tasks = self.tasks

        if status:
            filtered_tasks = [t for t in filtered_tasks if t.status == status]
            logger.debug("Filtered by status '%s': %d tasks", status, len(filtered_tasks))

        if priority:
            filtered_tasks = [t for t in filtered_tasks if t.priority == priority]
            logger.debug("Filtered by priority '%s': %d tasks", priority, len(filtered_tasks))

        return filtered_tasks

    def get_overdue_tasks(self) -> List[Task]:
        """Get all overdue tasks.

        Returns:
            List of overdue tasks
        """
        overdue = [task for task in self.tasks if task.is_overdue()]
        if overdue:
            logger.warning("Found %d overdue tasks", len(overdue))
        else:
            logger.info("No overdue tasks")
        return overdue
