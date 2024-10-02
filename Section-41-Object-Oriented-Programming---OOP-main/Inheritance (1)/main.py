class Person:
def __init__(self, name):
  self.phone_number = ""
   
def update_contact(self, new_number):
    self.phone_number = new_number
    print(f"The contact details have been updated to {self.phone_number} {self.address}")


class Customer(Person):
    def __init__(self):
        super().__init__()

    def purchase(self, item):
        print(f"{item} has been purchased")


new_customer = Customer()
new_customer.purchase("Coffe")
print(new_customer.phone_number)
new_customer.update_contact("222-111-3333")
