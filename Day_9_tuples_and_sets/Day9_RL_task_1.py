# 1. Min, Avg, Max
# Write a function get_min_avg_max (sequence) that returns a tuple with three values, the smallest, the arithmetic mean, and the largest value in the string, respectively.
# Example:
# get_min_avg_max ([0,10,1,9]) -> (0,5,10)
# the incoming sequence can be a tuple or a list with numeric values.
#
def get_min_avg_max_1a(my_set):
    num_sum=0
    nums_count=0
    for n in my_set:
        if type(n)==int:
            num_sum+=n
            nums_count+=1
    avg_val=round(num_sum/nums_count)
    return min(my_set),max(my_set), avg_val
my_set=tuple([0,10,1,9])
sum(tuple(my_set))
print(my_set, type(my_set))
min_value,max_value, avg_value=get_min_avg_max_1a(my_set)
print(min_value, max_value, avg_value)

# 1b for those more experienced
# Write a function get_min_med_max (sequence) that returns a tuple with three values, the smallest, the median, and the largest value from the string, respectively.
# The median value is the value that is in the middle of the sequence. If the number of strings is even then there are two values ​​in the middle.
# https://en.wikipedia.org/wiki/Median
# get_min_med_max ([1,5,8,4,3]) -> (1,4,8)
# get_min_med_max ([2,2,9,9,4,3]) -> (2,3.5,9)
# get_min_med_max ("baaac") -> ('a', 'a', 'c')
#  # with a string input we can have interesting results at an even number having an average, so it's better to give both averages
# get_min_med_max ("faaacb") -> ('a', 'ab', 'f')
# the incoming sequence can be a tuple or list with values of the same type, or even a string.
#

def get_min_med_max(my_set):
    my_list=list(my_set)
    my_list.sort()
    mid_idx=round(len(my_list)/2)
    if len(my_list) % 2==0:
        mid_value=my_list[mid_idx-1] + my_list[mid_idx]
    else:
        mid_value=my_list[mid_idx]

    return min(my_set),mid_value,max(my_set)
my_set=tuple("baaac")
print(f'{my_set=}, min, med, max = {get_min_med_max(my_set)}')

#print(min_value, max_value, avg_value)