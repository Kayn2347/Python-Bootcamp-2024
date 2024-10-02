import getpass
# Create database for username and password
database = {"elshad": "123456", "Renad": "654321"}
# Create variable for correct user and be default it is false
correct_user = False

while True:
    # Enter user name if the user name is not correct
    if not correct_user:
        username = input("Enter Your Username : ")
    # If user_name does not exist, continue to get new user_name
    if username not in database:
        print("User name is not correct!")
        continue
    # If user_name is correct set correct_user to True
    correct_user = True
    # Use getpass module instead of the input function to make sure that a user
    # does not get to see what they write in the password field.
    password = getpass.getpass("Enter Your Password : ")
    # If password is correct print success by executing break otherwise continue
    if database[username] != password:
        continue
    break
print("Success")

