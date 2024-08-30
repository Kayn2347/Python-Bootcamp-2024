# Docstrings

len()

def format_name(f_name, l_name):
    """This function formats first and last name"""
    if f_name == "" or l_name == "":
        return "Name or last name cannot be empty"
    formated_f_name =f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name},{formated_l_name}"


format_name()
"""comment comment  
dhdhdhdhdhd
"""