annual_salary = float(input("Enter the starting salary: "))

current_savings = 0
down_percent = .25
house_price = 1000000
semi_annual_raise = .07
r = .04
down_pay = house_price * down_percent
epsilon = 100
num_guesses = 0
low = 0
high = 10000
guess = (high+low) / 2.0
monthly_percent = guess/10000
adj_annual_salary = annual_salary
printout = True

while abs(current_savings - down_pay) > 100:
    current_savings = 0
    adj_annual_salary = annual_salary
    for i in range(1, 37):
        investment_returns = current_savings * r / 12
        monthly_salary = adj_annual_salary / 12
        monthly_savings = monthly_salary * monthly_percent
        current_savings = current_savings + monthly_savings + investment_returns
        if i % 6 == 0:
            adj_annual_salary = adj_annual_salary * (1 + semi_annual_raise)
    if current_savings < down_pay:
        low = guess
    else:
        high = guess
    print(current_savings)
    guess = (high+low) / 2
    if guess >= 9999:
        print("You can't save enough for a down payment! Even if you saved 99.99%, you'd fall short.")
        printout = False
        break
    monthly_percent = guess / 10000
    num_guesses += 1

if printout:
    print("Best savings rate:", round(monthly_percent, 4))
    print("Steps in bisection search:", num_guesses)
