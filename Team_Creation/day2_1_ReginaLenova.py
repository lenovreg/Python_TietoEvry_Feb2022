# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import datetime as dt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def age_100(name, age):
    #calculate and print when you will be at age 100
    if int(age) < 100:
        count_years = 100 - age
        return count_years

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    your_name=input('What is your name? ')
    print_hi(your_name)
    age=input(f'What is your age,  {your_name}?')
    int_age = int(age)
    print(f'Your age {int_age} {your_name}')
    years_after = age_100(your_name,int_age)
    print(f'Your will be 100 years old after {years_after} , {your_name}')

    print(f'Year now is {dt.datetime.now().year}')
    print(f'you will be at age 100 on {dt.datetime.now().year+years_after}')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
