# https://www.youtube.com/watch?v=hMlojBu3PIg

# Find the Missing Number
#sample_list1 = [0,1,2,3,4,5,7,8,9]
sample_list2 = [0,1,6,2,7,5,4]
#sample_list3 = [3,1,6,2,7,5,4]

sample_list = sorted(sample_list2)

missing_num = []
for num in range(sample_list[0], sample_list[-1] + 1):
    if num not in sample_list:
        missing_num.append(num)

print(missing_num)
