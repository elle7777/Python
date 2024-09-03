#Compound Interest
#version 0.1.0
#@Iustin Desrobitu

def compound_interest_calculator(principal_amount_in, interest_rate_in, interest_time_in):
    amount = principal_amount_in * pow((1 + interest_rate_in / 100), interest_time_in)
    compound_interest = amount - principal_amount
    return compound_interest

print("This program tekes the amount, interest rate (%) and years to calculate compound interest")
principal_amount = float(input("insert the amount: "))
interest_rate = float(input("insert the interest rate: "))
interest_time = int(input("insert thr interest time: "))

print(f"after {interest_time} year/s your intererst will be {compound_interest_calculator(principal_amount, interest_rate, interest_time)}")

