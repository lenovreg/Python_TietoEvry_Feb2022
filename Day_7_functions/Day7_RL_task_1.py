# 1. The Big Result
# Write an add_mult function that requires three parameters / arguments
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.
# PS Assume that numeric parameters will always be passed to the function, no need to check types
# Various solutions are possible (you are allowed to use other data structures inside function such as list).
# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30
#
def add_mult(a:int,b:int, c:int) -> int:
    num_list=[]
    num_list.append(a)
    num_list.append(b)
    num_list.append(c)
    num_list.sort()
    print('numbers ordered:',  num_list)
    return((num_list[0]+num_list[1])*num_list[2])

res=input("Input 3 numbers separated by comma: ")
num_list=res.split(",")
print(add_mult(int(num_list[0]),int(num_list[1]),int(num_list[2])))


