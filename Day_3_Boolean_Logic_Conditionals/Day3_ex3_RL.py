# 3. Ordered output.
#
# Ask the user to enter 3 numbers, output them in ascending order.
#
# Note: for now, we solve this task only with if, elif, else actions.
#
# There is also a solution using sorting and list structure, which we have not yet seen.
num_1 = float(input('Enter number 1:'))
num_2 = float(input('Enter number 2:'))
num_3 = float(input('Enter number 3:'))
if num_1 <= num_2 <= num_3:# num_1 is the smallest
    if num_2 <= num_3: # num_1 is the smallest
        print(f'order of numbers is (1) : {num_1},{num_2},{num_3}')
    else:
        print(f'order of numbers is (2): {num_1},{num_3},{num_2}')
elif num_3 <= num_2 <=num_1:# num_2 is the smallest
    if num_2 <=num_1 :
        print(f'order of numbers is (3): {num_3},{num_2},{num_1}')
    else:
        print(f'order of numbers is (4): {num_3},{num_1},{num_2}')
else:
    if num_2 <=num_3:
        print(f'order of numbers is (5): {num_2},{num_3},{num_1}')
    else:
        print(f'order of numbers is (6): {num_1},{num_3},{num_2}')