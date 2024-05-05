class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.description} (Срок: {self.due_date}) - {'Выполнено' if self.completed else 'Не выполнено'}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Задача добавлена: {new_task}")

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                print(f"Задача отмечена как выполненная: {task}")
                break
        else:
            print("Задача не найдена.")

    def show_current_tasks(self):
        print("Текущие задачи:")
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            for task in current_tasks:
                print(task)
        else:
            print("Нет текущих задач.")


manager = TaskManager()
manager.add_task("Купить продукты", "06-05-2024")
manager.add_task("Сдать проект", "05-05-2024")

manager.show_current_tasks()

manager.mark_task_completed("Купить продукты")

manager.show_current_tasks()