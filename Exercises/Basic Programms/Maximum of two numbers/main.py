#Maximum of two numbers
#version 0.1.0
#@Iustin Desrobitu

def max_number(first_number_in, second_number_in): #this function compares two numbers and outputs the biggest one
    if first_number_in > second_number_in:         #when the nambers are equa the function will output false
        return first_number_in
    if first_number_in < second_number_in:
        return second_number_in
    if first_number_in == second_number_in:
        return False

print("This program compares to numbers and finds the biggest")
first_number = float(input("insert the first number: ")) 
second_number = float(input("insert the second number: "))
if max_number(first_number, second_number): #this line verify if the numbers are equals
    #this formatted strings prints the result of the max_number function
    print(f"the biggest number is {max_number(first_number, second_number)}")
else:
    print("the numbers are equal")