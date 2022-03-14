# 1a. Average value
# Write a program that prompts the user to enter numbers (float).
# The program shows the average value of all entered numbers after each entry.
# PS. 1a can do without a list
# 1b. The program shows both the average value of the numbers and ALL the numbers entered
# PS Exit the program  by entering "q"
# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.
#
my_nums = []
while True:
    res=input("Enter some numbers (float) (numbers delimetered by ,); q to quit:")
    if res[0].lower()=='q':
        # do nothing
        print('Finish')
        break
    else:
        my_nums.append(res.split(","))
        print('list of numbers entered: ',my_nums)
        #print(type(my_nums))
        sum_nums=0
        count_nums=0
        for i,ll in enumerate(my_nums):
            #print(i)
            #print(ll, type(ll))
            for n in ll:
                sum_nums+=float(n)
                count_nums+=1
        print(f'Average amount of numbers entered is: {round(sum_nums/count_nums,2)}')

                #sum_nums+=round(float(nn[j]),2)
                #count_nums+=1
        #print(f'average of numbers entered is {round(sum_nums/count_nums,2)}')

        # for inner_list in my_nums:
        #    print(inner_list.strip())
        #    summa=sum(inner_list.strip())
        #    print(summa)
        # #my_nums.avgdfxxs