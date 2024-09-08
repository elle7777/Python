#Print all prime numbers
#version 0.1.0
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

def prime_compiler(min_range, max_range):
    counter = min_range
    prime_list = []
    while (counter < max_range + 1):
        if prime_check(counter):
            prime_list.append(counter)
        else:
            pass 
        counter += 1
    return prime_list

print("This program is takes two numbers and finds all prime numbers in between")
min_range = int(input("insert the minimum range: "))
max_range = int(input("insert the maximum range: "))

print(f"these are all the prime numbers between {min_range} and {max_range} {prime_compiler(min_range, max_range)}")
