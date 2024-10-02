class Person:
    def __init__(self, name):
        self.name = name
        self.phone_number = ""
        self.address = ""

    def update_contact(self, phone_number, address):
        self.phone_number = phone_number
        self.address = address
        print(f"The contact details have been updated to {self.phone_number} {self.address}")


class Employee(Person):
    def __init__(self, name, employee_number):
        super().__init__(name=name)
        self.employee_number = employee_number
        self.email = ""

    def promote(self):
        print(f"{self.name} has been promoted!")

    def retire(self):
        print(f"{self.name} has been retired!")

    def update_contact(self, phone_number, address):
        super().update_contact(phone_number=phone_number, address=address)



new_employee = Employee("Kayn", "100")
print(new_employee.email)
new_employee.update_contact("123-123", "1 Infinite loop", "Kaynlourence1210@gmail.com")
print(new_employee.email)
