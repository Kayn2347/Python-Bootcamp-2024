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

def withdraw(self, amount):
    if 0 < amount <= self.balance:
        self.balance -= amount
        print(f"${amount} is withdrawn from {self.name}'s bank account")
    else:
        print("Insufficient amount")
    self.show_balance()

def show_balance(self):
    print(f"Balance is ${self.balance}")


new_bank_account = BankAccount(ba_name="Kayn", ba_balance=0)
new_bank_account.deposit(2000000)
new_bank_account.withdraw(200000)

