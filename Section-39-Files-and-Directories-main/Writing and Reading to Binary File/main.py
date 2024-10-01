# with open('binary_file', 'bw') as b_file:
#    b_file.write(bytes(range(255)))

# with open('binary_file', 'br') as b_file:
#     for i in b_file:
#         print(i)

custom_number = 83747583938273747374292922873748593945994
with open('binary_file2', 'bw') as bin_file:
    bin_file.write(custom_number.to_bytes(20, byteorder='big'))

with open('binary_file2', 'br') as bin_file:
    a = int.from_bytes(bin_file.read(), byteorder='big')

print(a)
