#Armstrong Number
#version 0.1.0
#@Iustin Desrobitu

def index_separator(user_number_in, index):
    number_at_index = (user_number_in % 10 ** index) / 10 ** (index - 1)
    return(int(number_at_index))

def armstrong_number_check (user_number_in):
    index = len(str(user_number_in))
    user_number_length = len(str(user_number_in))
    armstrong_number = 0
    while index > 0:
        armstrong_number = armstrong_number + index_separator(user_number_in, index) ** user_number_length
        index = index - 1
    if armstrong_number == user_number_in:
        return True
    else:
        return False

print("This program take a number and check if it's an armstrong number")
user_number = int(input("insert a number: "))

if armstrong_number_check(user_number): 
    print(f"{user_number} is an armstrong number")
else:
    print(f"{user_number} is not an armstrong number")