class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def message_str(self):
        if self.completed == True:
            status = "Выполнено"
            print(f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}")
        else:
            status = "Не выполнено"
            print(f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}")

# Пример использования

print("\n")
task1 = Task("Купить фитинги", "11-07-2024")
task2 = Task("Сделать ДЗ", "11-07-2024")

task1.message_str()
task2.message_str()

task1.mark_completed()

print("\n")
task1.message_str()
task2.message_str()