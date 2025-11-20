"""Unit tests for the TaskManager class."""

import json
from datetime import datetime, timedelta

import pytest

from src.task_manager import TaskManager, TaskPriority, TaskStatus


@pytest.fixture
def temp_storage(tmp_path):
    """Create a temporary storage file for testing."""
    return tmp_path / "test_tasks.json"


@pytest.fixture
def task_manager(temp_storage):  # pylint: disable=redefined-outer-name
    """Create a TaskManager instance with temporary storage."""
    return TaskManager(storage_path=str(temp_storage))


class TestTaskManager:  # pylint: disable=too-many-public-methods
    """Test cases for the TaskManager class."""

    def test_init_creates_empty_task_list(self, task_manager):
        """Test that new TaskManager starts with empty task list."""
        assert len(task_manager.tasks) == 0
        assert task_manager.next_id == 1

    def test_add_task_basic(self, task_manager):
        """Test adding a basic task."""
        task = task_manager.add_task(title="Test Task")

        assert task.task_id == 1
        assert task.title == "Test Task"
        assert len(task_manager.tasks) == 1
        assert task_manager.next_id == 2

    def test_add_task_with_all_parameters(self, task_manager):
        """Test adding a task with all parameters."""
        task = task_manager.add_task(
            title="Complete Task",
            description="Full description",
            priority=TaskPriority.HIGH,
            due_date="2025-12-31",
        )

        assert task.title == "Complete Task"
        assert task.description == "Full description"
        assert task.priority == TaskPriority.HIGH
        assert task.due_date == "2025-12-31"

    def test_add_multiple_tasks_increments_id(self, task_manager):
        """Test that adding multiple tasks increments IDs correctly."""
        task1 = task_manager.add_task(title="Task 1")
        task2 = task_manager.add_task(title="Task 2")
        task3 = task_manager.add_task(title="Task 3")

        assert task1.task_id == 1
        assert task2.task_id == 2
        assert task3.task_id == 3
        assert len(task_manager.tasks) == 3

    def test_get_task_existing(self, task_manager):
        """Test getting an existing task."""
        added_task = task_manager.add_task(title="Find Me")
        found_task = task_manager.get_task(added_task.task_id)

        assert found_task is not None
        assert found_task.task_id == added_task.task_id
        assert found_task.title == "Find Me"

    def test_get_task_non_existing(self, task_manager):
        """Test getting a non-existing task returns None."""
        task = task_manager.get_task(999)
        assert task is None

    def test_update_task_title(self, task_manager):
        """Test updating a task's title."""
        task = task_manager.add_task(title="Original Title")
        success = task_manager.update_task(task.task_id, title="New Title")

        assert success is True
        updated_task = task_manager.get_task(task.task_id)
        assert updated_task.title == "New Title"

    def test_update_task_status(self, task_manager):
        """Test updating a task's status."""
        task = task_manager.add_task(title="Task")
        success = task_manager.update_task(task.task_id, status=TaskStatus.COMPLETED)

        assert success is True
        updated_task = task_manager.get_task(task.task_id)
        assert updated_task.status == TaskStatus.COMPLETED

    def test_update_task_multiple_fields(self, task_manager):
        """Test updating multiple fields at once."""
        task = task_manager.add_task(title="Task")
        success = task_manager.update_task(
            task.task_id,
            title="Updated",
            priority=TaskPriority.CRITICAL,
            status=TaskStatus.IN_PROGRESS,
            description="New description",
        )

        assert success is True
        updated_task = task_manager.get_task(task.task_id)
        assert updated_task.title == "Updated"
        assert updated_task.priority == TaskPriority.CRITICAL
        assert updated_task.status == TaskStatus.IN_PROGRESS
        assert updated_task.description == "New description"

    def test_update_task_non_existing(self, task_manager):
        """Test updating a non-existing task returns False."""
        success = task_manager.update_task(999, title="Should Fail")
        assert success is False

    def test_delete_task_existing(self, task_manager):
        """Test deleting an existing task."""
        task = task_manager.add_task(title="To Delete")
        initial_count = len(task_manager.tasks)

        success = task_manager.delete_task(task.task_id)

        assert success is True
        assert len(task_manager.tasks) == initial_count - 1
        assert task_manager.get_task(task.task_id) is None

    def test_delete_task_non_existing(self, task_manager):
        """Test deleting a non-existing task returns False."""
        success = task_manager.delete_task(999)
        assert success is False

    def test_list_tasks_no_filter(self, task_manager):
        """Test listing all tasks without filters."""
        task_manager.add_task(title="Task 1", priority=TaskPriority.LOW)
        task_manager.add_task(title="Task 2", priority=TaskPriority.HIGH)
        task3 = task_manager.add_task(title="Task 3")
        task_manager.update_task(task3.task_id, status=TaskStatus.COMPLETED)

        tasks = task_manager.list_tasks()
        assert len(tasks) == 3

    def test_list_tasks_filter_by_status(self, task_manager):
        """Test listing tasks filtered by status."""
        task_manager.add_task(title="Todo 1")
        task_manager.add_task(title="Todo 2")
        task3 = task_manager.add_task(title="Done")
        task_manager.update_task(task3.task_id, status=TaskStatus.COMPLETED)

        todo_tasks = task_manager.list_tasks(status=TaskStatus.TODO)
        assert len(todo_tasks) == 2
        assert all(t.status == TaskStatus.TODO for t in todo_tasks)

    def test_list_tasks_filter_by_priority(self, task_manager):
        """Test listing tasks filtered by priority."""
        task_manager.add_task(title="High 1", priority=TaskPriority.HIGH)
        task_manager.add_task(title="High 2", priority=TaskPriority.HIGH)
        task_manager.add_task(title="Low", priority=TaskPriority.LOW)

        high_tasks = task_manager.list_tasks(priority=TaskPriority.HIGH)
        assert len(high_tasks) == 2
        assert all(t.priority == TaskPriority.HIGH for t in high_tasks)

    def test_list_tasks_filter_by_status_and_priority(self, task_manager):
        """Test listing tasks filtered by both status and priority."""
        task_manager.add_task(
            title="Match",
            priority=TaskPriority.HIGH,
        )
        task2 = task_manager.add_task(
            title="No Match - Status",
            priority=TaskPriority.HIGH,
        )
        task_manager.update_task(task2.task_id, status=TaskStatus.COMPLETED)
        task_manager.add_task(
            title="No Match - Priority",
            priority=TaskPriority.LOW,
        )

        filtered = task_manager.list_tasks(
            status=TaskStatus.TODO,
            priority=TaskPriority.HIGH,
        )
        assert len(filtered) == 1
        assert filtered[0].title == "Match"

    def test_get_overdue_tasks_none(self, task_manager):
        """Test getting overdue tasks when there are none."""
        future_date = (datetime.now() + timedelta(days=7)).isoformat()
        task_manager.add_task(title="Future Task", due_date=future_date)

        overdue = task_manager.get_overdue_tasks()
        assert len(overdue) == 0

    def test_get_overdue_tasks_some(self, task_manager):
        """Test getting overdue tasks."""
        past_date = (datetime.now() - timedelta(days=7)).isoformat()
        future_date = (datetime.now() + timedelta(days=7)).isoformat()

        task_manager.add_task(title="Overdue 1", due_date=past_date)
        task_manager.add_task(title="Overdue 2", due_date=past_date)
        task_manager.add_task(title="Future", due_date=future_date)

        overdue = task_manager.get_overdue_tasks()
        assert len(overdue) == 2

    def test_persistence_save_and_load(self, temp_storage):
        """Test that tasks are persisted and loaded correctly."""
        # Create manager and add tasks
        manager1 = TaskManager(storage_path=str(temp_storage))
        manager1.add_task(title="Persist Task 1", priority=TaskPriority.HIGH)
        manager1.add_task(title="Persist Task 2", description="With description")

        # Create new manager with same storage
        manager2 = TaskManager(storage_path=str(temp_storage))

        # Verify tasks were loaded
        assert len(manager2.tasks) == 2
        assert manager2.tasks[0].title == "Persist Task 1"
        assert manager2.tasks[0].priority == TaskPriority.HIGH
        assert manager2.tasks[1].title == "Persist Task 2"
        assert manager2.tasks[1].description == "With description"
        assert manager2.next_id == 3

    def test_persistence_update_reflected(
        self, temp_storage
    ):  # pylint: disable=redefined-outer-name
        """Test that updates are persisted."""
        manager1 = TaskManager(storage_path=str(temp_storage))
        task = manager1.add_task(title="Original")
        manager1.update_task(task.task_id, title="Updated")  # type: ignore[arg-type]

        manager2 = TaskManager(storage_path=str(temp_storage))
        loaded_task = manager2.get_task(task.task_id)  # type: ignore[arg-type]

        assert loaded_task.title == "Updated"  # type: ignore[union-attr]

    def test_persistence_delete_reflected(
        self, temp_storage
    ):  # pylint: disable=redefined-outer-name
        """Test that deletions are persisted."""
        manager1 = TaskManager(storage_path=str(temp_storage))
        task = manager1.add_task(title="To Delete")
        manager1.delete_task(task.task_id)  # type: ignore[arg-type]

        manager2 = TaskManager(storage_path=str(temp_storage))

        assert len(manager2.tasks) == 0
        assert manager2.get_task(task.task_id) is None  # type: ignore[arg-type]

    def test_corrupted_json_raises_error(self, temp_storage):
        """Test that corrupted JSON file raises appropriate error."""
        # Write invalid JSON
        with open(temp_storage, "w", encoding="utf-8") as f:
            f.write("{invalid json content")

        with pytest.raises(json.JSONDecodeError):
            TaskManager(storage_path=str(temp_storage))
