class BankAccount:

def __init__(self, ba_name, ba_balance):
    self.name = ba_name
    self.balance = ba_balance


new_bank_account = BankAccount(ba_name="Kayn", ba_balance=0)
print(new_bank_account)