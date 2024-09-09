#Largest number in an Array
#version 0.1.0
#@Iustin Desrobitu

def float_converter(number_list):
    new_list = []
    for number in number_list:
        new_list.append(float(number))
    return new_list

def largest_number_finder(number_list):
    float_list = float_converter(number_list) 
    largest_number = 0
    for number in float_list:
        if number > largest_number:
            largest_number = number
    return largest_number

print("this program takes an array of numbers (separated by spaces) and finds the largest")
number_list = str(input("insert a list of numbers: "))
number_list = number_list.split(" ", -1) 

print(f"The largest number is {largest_number_finder(number_list)}")

