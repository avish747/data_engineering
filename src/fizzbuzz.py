"""
Write a program that prints the numbers from 1 to n.
But for multiples of 3, print 'Fizz' instead of the number, and for multiples of 5, print 'Buzz'.
For numbers that are multiples of both 3 and 5, print 'FizzBuzz'.
"""



def print_fizz_buzz(num):
    for number in range(1, int(num)+1):
        output = ""
        if number%3 == 0:
            output += "Fizz"
        if number%5 == 0:
            output += "Buzz"
        print(output or number)


num = input("Provide the Number")
print_fizz_buzz(num)
