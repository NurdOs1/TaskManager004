from typing import List

class Task:
    def __init__(self, title: str, description: str):
        # Инициализация закрытых атрибутов задачи
        self.__title = title
        self.__description = description

    @property
    def title(self) -> str:
        # Возвращает название задачи
        return self.__title

    @property
    def description(self) -> str:
        # Возвращает описание задачи
        return self.__description

    def update_title(self, new_title: str):
        # Обновляет название задачи
        self.__title = new_title

    def update_description(self, new_description: str):
        # Обновляет описание задачи
        self.__description = new_description

class TaskManager:
    def __init__(self):
        # Инициализация закрытого списка задач
        self.__tasks: List[Task] = []

    def add_task(self, title: str, description: str):
        # Добавляет задачу в список
        task = Task(title, description)
        self.__tasks.append(task)

    def remove_task(self, index: int):
        # Удаляет задачу по индексу
        if 0 <= index < len(self.__tasks):
            del self.__tasks[index]
        else:
            raise IndexError("Invalid task index")

    def get_task(self, index: int) -> Task:
        # Возвращает задачу по индексу
        if 0 <= index < len(self.__tasks):
            return self.__tasks[index]
        else:
            raise IndexError("Invalid task index")

    @property
    def tasks(self) -> List[Task]:
        # Возвращает копию списка задач
        return self.__tasks.copy()

# Пример использования:
if __name__ == "__main__":
    # Создаем объект TaskManager
    task_manager = TaskManager()

    # Добавляем задачи
    task_manager.add_task("Задача 1", "Описание 1")
    task_manager.add_task("Задача 2", "Описание 2")

    # Получаем и выводим список задач
    tasks = task_manager.tasks
    for idx, task in enumerate(tasks, start=1):
        print(f"Задача {idx}: {task.title} - {task.description}")

    # Пример удаления задачи
    task_manager.remove_task(0)

    # Получаем и выводим обновленный список задач
    tasks = task_manager.tasks
    for idx, task in enumerate(tasks, start=1):
        print(f"Задача {idx}: {task.title} - {task.description}")
