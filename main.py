from task_manager import TaskManager
from datetime import datetime


def main():
    manager = TaskManager()

    while True:
        print("\nМеню:")
        print("1. Просмотр задач")
        print("2. Добавить задачу")
        print("3. Выполнить задачу")
        print("4. Редактировать задачу")
        print("5. Удалить задачу")
        print("6. Поиск задач")
        print("7. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            # Просмотр задач
            for task in manager.tasks:
                print(task)

        elif choice == "2":
            # Добавление задачи
            title = input("Название задачи: ")
            description = input("Описание: ")
            category = input("Категория: ")
            due_date_str = input("Срок выполнения (YYYY-MM-DD): ")
            priority = input("Приоритет (0, 1, 2): ")
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
                manager.add_task({
                    "title": title,
                    "description": description,
                    "category": category,
                    "due_date": due_date,
                    "priority": priority,
                    "status": "Не выполнена"
                })
                print("Задача добавлена!")
            except ValueError:
                print("Неверный формат даты.")

        elif choice == "3":
            # Выполнить задачу
            task_id = int(input("ID задачи: "))
            task = manager.find_task(task_id)
            if task:
                task.mark_complete()
                manager.save_tasks()
                print("Задача выполнена!")
            else:
                print("Задача не найдена.")

        elif choice == "4":
            # Редактировать задачу
            task_id = int(input("ID задачи: "))
            if manager.edit_task(task_id):
                print("Задача отредактирована!")
            else:
                print("Редактирование невозможно!")


        elif choice == "5":
            # Удалить задачу
            task_id = int(input("ID задачи: "))
            manager.delete_task(task_id)
            print("Задача удалена!")

        elif choice == "6":
            # Поиск задач
            keyword = input("Введите ключевое слово для поиска: ")
            results = [task for task in manager.tasks if keyword.lower() in task.title.lower()]
            for task in results:
                print(task)
        elif choice == "7":
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()
