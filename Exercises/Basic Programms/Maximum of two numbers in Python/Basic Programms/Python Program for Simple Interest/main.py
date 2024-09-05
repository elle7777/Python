#Simple interst calculator
#version 0.1.0
#@Iustin Desrobitu

def simple_interest_calculator(user_amount_in, user_rate_in, user_years_in):
    interest_rate = (user_amount_in * user_years_in * user_rate_in) / 100
    return interest_rate

print("This program tekes the amount, interest rate (%) and years to calculate simple interest")
user_amount = float(input("insert the amount: "))
user_rate = float(input("insert the rate: "))
user_years = int(input("insert the number of yaers: "))
print(f"after {user_years} year/s your intererst will be {simple_interest_calculator(user_amount, user_rate, user_years)}")
