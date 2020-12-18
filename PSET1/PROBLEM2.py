annual_salary = float(input("What's your annual salary? "))
portion_saved = .01 * float(input("What % of your salary do you want to save per month? "))
total_cost = float(input('How much does your dream home cost? '))
semi_annual_raise = .01 * float(input("What % semi-annual raise do you expect? "))
portion_down_payment = .25
total_down_payment = total_cost * portion_down_payment
current_savings = 0
r = .04
count = 0
while current_savings < total_down_payment:
    investment_returns = current_savings * r / 12
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary * portion_saved
    current_savings = current_savings + monthly_savings + investment_returns
    count += 1
    if count % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
    print("Your current savings:", current_savings)
print("It will take you", count, 'months to save that much.')
