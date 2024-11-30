import json
import os
import datetime
from typing import List

from task import Task, TaskData


class TaskManager:
    def __init__(self, data_file="tasks.json"):
        self.data_file = data_file
        self.tasks: List[Task] = self.load_tasks()
        self.next_id = self.get_next_id()

    def load_tasks(self) -> List[Task]:
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                try:
                    tasks_data = json.load(f)
                    return [Task(task_data) for task_data in tasks_data]
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        with open(self.data_file, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def get_next_id(self) -> int:
        if self.tasks:
            return max(task.id for task in self.tasks) + 1
        return 1

    def add_task(self, task_data: TaskData):
        task_data["id"] = self.next_id
        self.next_id += 1
        new_task = Task(task_data)
        self.tasks.append(new_task)
        self.save_tasks()

    def find_task(self, task_id: int) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def edit_task(self, task_id: int) -> bool:
        task = self.find_task(task_id)
        if task:
            title = input("Введите новое название задачи (Enter, если хотите оставить прежним): ")
            description = input("Введите новое описание (Enter, если хотите оставить прежним): ")
            category = input("Введите новую категорию (Enter, если хотите оставить прежней): ")
            due_date_str = input("Введите новый срок выполнения (YYYY-MM-DD) (Enter, если хотите оставить прежним): ")
            priority = input("Введите новый приоритет (0, 1, 2) (Enter, если хотите оставить прежним): ")
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
                if title: task.title = title
                if description: task.description = description
                if category: task.category = category
                if due_date_str: task.due_date = due_date
                if priority: task.priority = priority
                print("Задача обновлена!")
            except ValueError:
                print("Неверный формат даты.")
                return False
            return True

        return False

    def delete_task(self, task_id: int):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()
