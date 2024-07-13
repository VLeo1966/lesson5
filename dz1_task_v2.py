class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline,'description': description,'status': "не выполненно"})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "выполненно"
                print(f"Задача: {description} выполнена")
            else:
                print(f"Задача: {description} не найдена")

    def show_tasks(self):
        print(f"Текущие задачи:")
        for task in self.tasks:
            if task['status'] == "не выполненно":
                print(f"{task['description']} - {task['deadline']}")

t = Task()
t.add_task("01.06.2023", "прочитать книгу")
t.add_task("05.05.2023", "пробежать марафон")
t.add_task("27.06.2023", "починить машину")

t.show_tasks()

t.complete_tasks("прочитать книгу")
