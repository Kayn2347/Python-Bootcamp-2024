alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def refactor_position(p_position, p_cipher_type):
    if p_cipher_type == 'E':
        while p_position > 25:
            p_position = p_position - 26
        return p_position
    else:
        while p_position < 0:
            p_position = p_position + 26
        return p_position

def caesar_chiper(p_initial_text, p_shift_amount, p_cipher_type):
  final_text = ""
  if p_cipher_type == "D":
    p_shift_amount *= -1
  for char in p_initial_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + p_shift_amount
      new_position = refactor_position(new_position, p_cipher_type)
      final_text += alphabet[new_position]
    else:
      final_text += char
  print(f"Here's the {'decode' if p_cipher_type=='D' else 'encode'}d result: {final_text}")



from logo import logo
print(logo)

end_program = False
while not end_program:
  enc_dec = input("Type 'E' to encrypt, type 'D' to decrypt:\n")
  text = input("Enter your message:\n").upper()
  shift = int(input("Enter the shift number:\n"))
  caesar_chiper(p_initial_text=text, p_shift_amount=shift, p_cipher_type=enc_dec)
  restart = input("Type 'Y' if you want to go again. Otherwise type 'N'.\n")
  if restart == "N":
    end_program = True
    print("See you next time!")