import random

class Person:
  def __init__(self, name, phone_number, address):
    self.name = name
    self.phone_number = phone_number
    self.address = address
   
  def update_contact(self, new_number):
    self.phone_number = new_number
    print(f"The contact details have been updated to {self.phone_number} ")


class Customer(Person):
    def __init__(self, name):
        super().__init__(name=name, phone_number="", address="")
        self.customer_id = random.randint(1, 100)

    def purchase(self, item):
        print(f"{item} has been purchased")


new_customer = Customer("kayn")
print(new_customer.name)
print(new_customer.customer_id)