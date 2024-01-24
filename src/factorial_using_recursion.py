def factorial(num, running_product):
    print("num : " + str(num))
    # Base Case
    if int(num) == 1:
        print("Reached Base Case")
        return running_product
    elif num != 1:
        print("pre running_product : " + str(running_product))
        running_product = running_product * num
        num -= 1
        print("post running_product : " + str(running_product))
        return factorial(num, running_product)

print(factorial(5, 1))