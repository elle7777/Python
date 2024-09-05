#Add two numbers
#version 0.1.0
#@Iustin Desrobitu

def addition(first_number_in, second_number_in): #this functions add two numbers
    return first_number_in + second_number_in #and returns the result

print("This programm adds two numbers")
#I used float to account for the user inputing decimal values
first_number = float(input("insert the first number: ")) 
second_number = float(input("insert the second number: "))
#this line prints the results using a formatted line
print(f"{first_number} + {second_number} = {addition(first_number, second_number)}") 