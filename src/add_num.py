# https://www.youtube.com/watch?v=F6HTQP3oDJA
# List with numbers and return True from the list if sum of any two numbers will be zero

sample_list = [1, 2, 3, 4, -1, -2, 0]
#sample_list = [-8, -9, -10, -11, 0, 1, 2, 3, 4, 5, 6, 7]
sorted_sample_list = sorted(sample_list)
positive_list = [number for number in sorted_sample_list if number > 0]
negative_list = [number for number in sorted_sample_list if number <= 0]
for num in negative_list:
    if abs(num) in positive_list:
        print("Success")
        break

