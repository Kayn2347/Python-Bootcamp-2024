class Customer:
    def__init__(self, name, balance):
        self.name = name 
        self.set_balance(balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance < 0:
          self.__balance = 0
        elif balance > 10000
          self.__balance = 10000
        else:
            self.__balance = balance

    balance = property(get_balance, set_balance)

customer1 = Customer("kayn", -1)
print(customer1.balance)
print(customer1.get_balance())
customer1.balance = 100