import sys
from datetime import datetime

# Perform String Compression in below way
# Input1  : aaabbcccdd
# Output1 : a3b2c3d2

# Input2  : aaddcceff
# Output2 : a2d2c2e1f2

user_input = str(input("Please enter your string for compression"))
user_input_length = len(user_input)
index = 0
compress_counter = 1
output_string = ""
while index < (user_input_length - 1):
    if user_input[index] == user_input[index + 1]:
        compress_counter += 1
        if index == (user_input_length - 2):
            output_string = output_string + user_input[index] + str(compress_counter)
            break
    elif user_input[index] != user_input[index + 1]:
        output_string = output_string + user_input[index] + str(compress_counter)
        compress_counter = 1
    index += 1

print(output_string)