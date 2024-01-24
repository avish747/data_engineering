input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sum of Even, Odd and Divisible by 3

def return_sum(identifier_func, input_list):
    sum=0
    for element in input_list:
        if identifier_func(element):
            sum += element
    return sum

odd_finder = lambda x:x%2 != 0
even_finder = lambda x:x%2 == 0
div_by_3 = lambda x:x%3 == 0

print("Sum of Odd : " + str(return_sum(odd_finder, input_list)))
print("Sum of Even : " + str(return_sum(even_finder, input_list)))
print("Sum of Div_by_3 : " + str(return_sum(div_by_3, input_list)))


