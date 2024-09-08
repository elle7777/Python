#Check Fibonacci Numeber
#version 0.1.0
#@Iustin Desrobitu

import math

def perfect_square_checker(number, original_number):
    squared_number = int(math.sqrt(number))
    powered_number = squared_number * squared_number
    if powered_number == number:
        return True
    else:
        return False

def fibonacci_checker(number):
    checker_1 = (5 * math.pow(number, 2)) + 4
    checker_2 = (5 * math.pow(number, 2)) - 4
    if perfect_square_checker(checker_1, number) or perfect_square_checker(checker_2, number):
        return True


print("This number checks is a number is a Fibonacci number")
number = int(input("insert a number: "))

if fibonacci_checker(number):
    print(f"{number} is a Fibonacci number")
else:
    print(f"{number} is not a Fibonacci number")