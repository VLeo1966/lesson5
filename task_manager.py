class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

# Пример использования
task1 = Task("Купить фитинги", "11-07-2024")
task2 = Task("Сделать ДЗ", "11-07-2024")

print("Созданные задачи:")
print(task1)
print(task2)

task1.mark_completed()

print("\nЗадачи после выполнения первой задачи:")
print(task1)
print(task2)