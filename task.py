from typing import TypedDict


class TaskData(TypedDict):
    id: int
    title: str
    description: str
    category: int
    due_date: str
    priority: str
    status: str


class Task:
    def __init__(self, task_data: TaskData):
        self.id = task_data["id"]
        self.title = task_data["title"]
        self.description = task_data["description"]
        self.category = task_data["category"]
        self.due_date = task_data["due_date"]
        self.priority = task_data["priority"]
        self.status = task_data["status"]

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}')"

    def mark_complete(self):
        if self.status == "Выполнена":
            print("Задача уже выполнена!")
        self.status = "Выполнена"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
        }
