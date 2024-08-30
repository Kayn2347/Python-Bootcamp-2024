def password_controller(password):
  if len(password) > 8:
      return "Success"
  else:
      return "The password has to be more than 8 characters"

result = password_controller("1234")
print(result)