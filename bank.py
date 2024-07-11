
class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили баланс. На счете {self.balance} рублей")

    def withdraw(self, money):
         if money > self.balance:
             print("Недостаточно средств на счете")
         elif money <= self.balance:
             self.balance -= money
             print(f"Вы успешно сняли {money} рублей. На счете: {self.balance} рублей")

    def all_balance(self):
        print(f"Ваш текущий баланс: {self.balance} рублей")

man = Account(id = "1234567890", balance = 600)
man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)