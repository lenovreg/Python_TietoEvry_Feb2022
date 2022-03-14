# 2. Cubes
# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)
# Output
# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125
# All cubes: [8,27,64,125]

res=input('Input range of numbers separated by comma - for example, 2,8: ')
my_range=res.split(",")
my_cubes=[]
num_start=int(my_range[0])
num_end=int(my_range[1])
my_cubes= [n*n*n for n in range(num_start, num_end+1)]
print('All_cubes: ', my_cubes)
