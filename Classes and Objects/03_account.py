class Account:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


# Example usage:
account1 = Account(123, "Alice", 1000)
print(account1.credit(500))  # Output: 1500
print(account1.debit(200))  # Output: 1300
print(account1.debit(2000))  # Output: Amount exceeded balance
print(account1.info())  # Output: User Alice with account 123 has 1300 balance
