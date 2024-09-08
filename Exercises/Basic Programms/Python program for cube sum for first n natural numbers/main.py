#Sum of Cubes
#version 0.1.0
#@Iustin Desrobitu

def squares_sum(number):
    index = 0
    sum = 0
    while index < number + 1:
        sum = sum + index ** 3
        index += 1
    return sum
        

print("This program takes a number and find the sum of the first Nth natural numbers")
number = int(input("insert a number: "))

print(f"the Cube sum of {number} is {squares_sum(number)}")