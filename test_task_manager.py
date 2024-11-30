from task_manager import TaskManager, TaskData
import os


def test_add_task():
    manager = TaskManager("test_tasks.json")

    task_data: TaskData = {
        "title": "Test Task",
        "description": "This is a test task",
        "category": "Test",
        "due_date": "2024-03-15",
        "priority": "Высокий",
        "status": "Не выполнена"
    }

    manager.add_task(task_data)
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Test Task"

    os.remove("test_tasks.json")


def test_delete_task():
    manager = TaskManager("test_tasks.json")

    task_data: TaskData = {
        "title": "Test Task",
        "description": "This is a test task",
        "category": "Test",
        "due_date": "2024-03-15",
        "priority": "Высокий",
        "status": "Не выполнена"
    }

    manager.add_task(task_data)
    manager.delete_task(1)
    assert len(manager.tasks) == 0

    os.remove("test_tasks.json")
