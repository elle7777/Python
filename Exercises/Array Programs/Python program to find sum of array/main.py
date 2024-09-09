#Sum of Array
#version 0.1.0
#@Iustin Desrobitu

def int_converter(number_list):
    new_list = []
    for number in number_list:
        new_list.append(int(number))
    return new_list

def array_adder(number_list):
    array_sum = 0
    int_list = int_converter(number_list)
    for number in int_list:
        array_sum += number
    return array_sum

print("This program takes a list of numners (separated be spaces) and sums them together")
number_list = str(input("insert a list of numbers: "))
number_list = number_list.split(" ", -1) 

print(f"The sum of the array is {array_adder(number_list)}")

