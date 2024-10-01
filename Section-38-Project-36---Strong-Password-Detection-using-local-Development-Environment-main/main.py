import re


# TODO 1 - Create function which takes 1 parameter
def strong_password_checker(password):
    is_strong = True
    # TODO 2 - Check for length of password
    if len(password) < 8:
        print("The password must be at least 8 characters long!")
        is_strong = False
    # TODO 3 - Create regex for lowercase
    lower_reg = re.compile(r'[a-z]')
    if not(lower_reg.search(password)):
        print("The password must include at least 1 lowercase!")
        is_strong = False
    # TODO 4 - Create regex for uppercase
    upper_reg = re.compile(r'[A-Z]')
    if not(upper_reg.search(password)):
        print("The password must include at least 1 uppercase!")
        is_strong = False
    # TODO 5 - Create regex for digits
    digit_reg = re.compile(r'\d')
    if not(digit_reg.search(password)):
        print("The password must include at least 1 digit!")
        is_strong = False
    # TODO 6 - Create regex for special characters
    special_reg = re.compile(r'[!@#$%^&*()|\\]')
    if not(special_reg.search(password)):
        print("The password must include at least 1 special character")
        is_strong = False
    # TODO 7 - If any of this returns none print message to the console
    if is_strong:
        print("The password is strong!")


strong_password_checker("1aW%hdgsuey53647")