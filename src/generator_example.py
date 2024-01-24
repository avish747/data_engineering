input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def generate_num(input_list):
    for element in input_list:
        yield element

my_generator = generate_num(input_list)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))