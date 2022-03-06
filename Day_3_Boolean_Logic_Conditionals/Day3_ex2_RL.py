# 2. Xmas Bonus
# # The company has promised a Christmas bonus in the amount of 15% of the monthly salary
# #for EVERY year of service over 2 years.
# # Task. Ask the user for the amount of the monthly salary and the number of years worked.
# # Calculate the bonus.
# # Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.
# # Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0).
#
empl_salary=float(input('Your salary (999.99)?'))
empl_years_working = float(input('How many years you have been working for The company (amount in years)?'))
if empl_years_working > 2:
    empl_salary = round(empl_salary,2)
    empl_years_working=round(empl_years_working)
    if empl_years_working == 2:
        empl_bonus = round(1 * empl_salary * 0.15,2) # if working 2.1 years, it would be over 2 years
    else:
        empl_bonus = round((empl_years_working - 2) * empl_salary * 0.15, 2)
    print(f'{empl_years_working} years of experience, {empl_salary} Euro salary, the bonus will be {empl_bonus} Euro.')
else:
    empl_bonus = 0
    print(f'{empl_years_working} years of experience, {empl_salary} Euro salary, no bonus ({empl_bonus}).')

