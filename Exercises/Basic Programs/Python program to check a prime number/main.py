#Prime number checker
#version 0.1.1
#@Iustin Desrobitu

def prime_check(number): 
    division_counter = number
    prime_check_counter = 0
    while(division_counter > 1):
        if number % division_counter > 0:
            pass
        else:
            prime_check_counter += 1
        division_counter -= 1
    if prime_check_counter < 2:
        return True
    else: 
        return False
    
print("This program takes a number and tells you if its a prime number")
number = int(input("enter a number: "))

if prime_check(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
