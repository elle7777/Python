#Fibonacci number
#verion 0.1.0
#@Iuststin Desrobitu

def fibonacci_generator(nth_term):
    fibonacci_sequence = [0, 1]
    index = 1
    while(index < nth_term):
        new_fibonacci = fibonacci_sequence[index - 1] + fibonacci_sequence[index]
        fibonacci_sequence.append(new_fibonacci)
        index = index + 1
    return fibonacci_sequence[nth_number]

print("This program takes an index and finds the corresponding number in the fibonacci sequence")
nth_number = int(input("insert an index: "))

print(f"the {nth_number}-th Fibonacci number is {fibonacci_generator(nth_number)}")