#Fractional of a number
#version 0.1.0
#@IustinDesrobitu

def factorial_calculator(user_number_in):
    factorial = user_number_in
    n = user_number_in - 1
    while(n > 0):
        factorial = factorial * (user_number_in - n)
        n = n - 1
    return factorial
        

print("This program find the factorial of a number")
user_number = int(input("insert a number (interger): "))

print(f"the factorial of {user_number} is {factorial_calculator(user_number)}")
