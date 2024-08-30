
def format_name(f_name, l_name): 
    if  f_name== "" or l_name== "":
      return "Name or last name cannot be empty"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name},{formated_l_name}"

first_name = input("Enter Name:")
second_name = input("Enter Sname: ")
output = format_name(first_name, second_name)
print(output)