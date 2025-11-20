"""Unit tests for the Task class and related functionality."""

import pytest
from datetime import datetime, timedelta
from src.task_manager import Task, TaskPriority, TaskStatus


class TestTask:
    """Test cases for the Task class."""

    def test_task_creation_with_defaults(self):
        """Test creating a task with default values."""
        task = Task(title="Test Task")

        assert task.title == "Test Task"
        assert task.description == ""
        assert task.priority == TaskPriority.MEDIUM
        assert task.status == TaskStatus.TODO
        assert task.due_date is None
        assert task.task_id is None
        assert task.created_at is not None
        assert task.updated_at == task.created_at

    def test_task_creation_with_all_fields(self):
        """Test creating a task with all fields specified."""
        due_date = "2025-12-31"
        task = Task(
            title="Important Task",
            description="This is a detailed description",
            priority=TaskPriority.HIGH,
            status=TaskStatus.IN_PROGRESS,
            due_date=due_date,
            task_id=42,
        )

        assert task.title == "Important Task"
        assert task.description == "This is a detailed description"
        assert task.priority == TaskPriority.HIGH
        assert task.status == TaskStatus.IN_PROGRESS
        assert task.due_date == due_date
        assert task.task_id == 42

    def test_task_creation_strips_whitespace(self):
        """Test that task title and description are stripped of whitespace."""
        task = Task(title="  Spaced Title  ", description="  Spaced Description  ")

        assert task.title == "Spaced Title"
        assert task.description == "Spaced Description"

    def test_task_creation_empty_title_raises_error(self):
        """Test that creating a task with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            Task(title="")

        with pytest.raises(ValueError, match="Task title cannot be empty"):
            Task(title="   ")

    def test_task_to_dict(self):
        """Test converting a task to dictionary."""
        task = Task(
            title="Test Task",
            description="Description",
            priority=TaskPriority.HIGH,
            task_id=1,
        )

        task_dict = task.to_dict()

        assert task_dict["task_id"] == 1
        assert task_dict["title"] == "Test Task"
        assert task_dict["description"] == "Description"
        assert task_dict["priority"] == TaskPriority.HIGH
        assert task_dict["status"] == TaskStatus.TODO
        assert "created_at" in task_dict
        assert "updated_at" in task_dict

    def test_task_from_dict(self):
        """Test creating a task from dictionary."""
        data = {
            "task_id": 5,
            "title": "From Dict Task",
            "description": "Created from dict",
            "priority": TaskPriority.CRITICAL,
            "status": TaskStatus.COMPLETED,
            "due_date": "2025-12-31",
            "created_at": "2025-01-01T12:00:00",
            "updated_at": "2025-01-02T12:00:00",
        }

        task = Task.from_dict(data)

        assert task.task_id == 5
        assert task.title == "From Dict Task"
        assert task.description == "Created from dict"
        assert task.priority == TaskPriority.CRITICAL
        assert task.status == TaskStatus.COMPLETED
        assert task.due_date == "2025-12-31"
        assert task.created_at == "2025-01-01T12:00:00"
        assert task.updated_at == "2025-01-02T12:00:00"

    def test_is_overdue_no_due_date(self):
        """Test that task without due date is not overdue."""
        task = Task(title="No Due Date")
        assert task.is_overdue() is False

    def test_is_overdue_future_date(self):
        """Test that task with future due date is not overdue."""
        future_date = (datetime.now() + timedelta(days=7)).isoformat()
        task = Task(title="Future Task", due_date=future_date)
        assert task.is_overdue() is False

    def test_is_overdue_past_date(self):
        """Test that task with past due date is overdue."""
        past_date = (datetime.now() - timedelta(days=7)).isoformat()
        task = Task(title="Overdue Task", due_date=past_date, status=TaskStatus.TODO)
        assert task.is_overdue() is True

    def test_is_overdue_completed_task(self):
        """Test that completed task is not considered overdue even if past due date."""
        past_date = (datetime.now() - timedelta(days=7)).isoformat()
        task = Task(
            title="Completed Task",
            due_date=past_date,
            status=TaskStatus.COMPLETED,
        )
        assert task.is_overdue() is False

    def test_is_overdue_invalid_date_format(self):
        """Test that invalid date format returns False."""
        task = Task(title="Invalid Date", due_date="not-a-date")
        assert task.is_overdue() is False
