from functools import reduce
"""
Let's explore the inbuilt high order functions of Python
1. Map
2. Filter
3. Reduce
"""

# Map
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
multiply_by_2 = map(lambda x:x*2, input_list)
divisible_by_2 = map(lambda x:x%2 == 0, input_list)
print(list(multiply_by_2))
print(list(divisible_by_2))

# Filter
filter_evens = filter(lambda x:x%2 == 0, input_list)
print(list(filter_evens))

# Reduce
find_sum = reduce(lambda x,y : x+y, input_list)
print(find_sum)