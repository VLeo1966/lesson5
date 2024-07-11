class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, price):
        if item_name in self.items:
            self.items[item_name] = price

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Товары: {self.items}"

# Создание объектов класса Store
store1 = Store("Магазин А", "ул. Ленина, 1")
store2 = Store("Магазин Б", "ул. Гагарина, 2")
store3 = Store("Магазин В", "ул. Пушкина, 3")

# Добавление товаров
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("апельсины", 0.8)
store2.add_item("груши", 1.0)

store3.add_item("виноград", 1.2)
store3.add_item("манго", 1.5)

# Тестирование методов
print(store1)
store1.update_price("яблоки", 0.55)
print(f"Изменилась цена яблок: {store1.get_price('яблоки')}")
print(f"Реализовали бананы: {store1.remove_item('бананы')}")
print(store1)

print("\n")

print(store2)
store2.update_price("апельсины", 0.85)
print(f"Изменилась цена апельсины: {store2.get_price('апельсины')}")
print(f"Реализовали груши: {store2.remove_item('груши')}")
print(store2)
