class BankAccount:

def __init__(self, ba_name, ba_balance):
    self.name = ba_name
    self.balance = ba_balance

def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        print(f"${amount} is deposited in {self.name}'s bank account.")
    else:
        print("Insufficient amount")
    self.show_balance()

