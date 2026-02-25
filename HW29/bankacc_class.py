# Работа с банковскими счетами, классами и методами

# Создаём класс "Банковский счет" с аттрибутами
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number  # номер счёта
        self.owner = owner  # имя владельца
        self.balance = balance  # баланс счёта
        print(f"Создан счёт №{account_number} для {owner}. Баланс: {balance} руб.")

# Определяем методы работы со счетами
    def deposit(self, amount):  # метод пополнения счёта
        if amount > 0:
            self.balance += amount
            print(f"Пополнение счёта №{self.account_number}: +{amount} руб. Новый баланс: {self.balance} руб.")
        else:
            print("Сумма пополнения должна быть положительной!")

    def withdraw(self, amount):  # метод снятия денег со счёта
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие со счёта №{self.account_number}: -{amount} руб. Новый баланс: {self.balance} руб.")
            else:
                print(f"Недостаточно средств на счёте №{self.account_number}! Баланс: {self.balance} руб.")
        else:
            print("Сумма снятия должна быть положительной!")

    def get_balance(self):  # метод получения текущего баланса
        return f"Баланс счёта №{self.account_number} (владелец: {self.owner}): {self.balance} руб."


# Создание нескольких объектов класса BankAccount
account1 = BankAccount("123321", "Иван Петров", 1000)
account2 = BankAccount("456654", "Елизавета Краснова", 500)
account3 = BankAccount("789987", "Пётр Иванов", 2000)

# Вызов методов для каждого объекта
print("\n--- Операции с счётом Ивана Петрова ---")
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)  # попытка снять больше, чем есть на счёте
print(account1.get_balance())

print("\n--- Операции с счётом Елизаветы Красновой ---")
account2.deposit(300)
account2.withdraw(100)
account2.deposit(200)
print(account2.get_balance())

print("\n--- Операции с счётом Петра Иванова ---")
account3.withdraw(700)
account3.deposit(1000)
account3.withdraw(500)
print(account3.get_balance())