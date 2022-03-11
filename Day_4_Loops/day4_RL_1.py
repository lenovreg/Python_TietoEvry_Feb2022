#  while True:
# #     res = input("Enter number or q to quit ")
# # #     if res.lower().startswith("q"): # more lenient any word starting with Q or q will work to quit
# #     if res == "q":
# #         print("No more calculations today. I am breaking out of the loop.")
# #         break
# #     elif len(res) == 0:  # so i had an empty string here...
# #         print("Hey! You just pressed Enter, please enter something...")
# #         continue # we go back to line 83 and start over
# #     # elif res == "a":  # TODO check if if the input is text
# #     elif res[0].isalpha():  # we are checking here for the first symbol of our input
# #         print("I can't cube a letter ")
# #         continue # means we are not going to try to convert "a" to float
# #         # in other words we are not going to do the below 4 instructions
# #     num = float(res)

while True:
    skaitlis=input('Input a number, q to quit!')
    if skaitlis.lower().startswith('q'):
        print('End of the game.')
        break
    elif len(skaitlis)==0:
        print('Non zero number is needed or q to quit!')
        continue
    elif skaitlis[0].isalpha():
        print('Number is needed or q to quit!')
        continue
    else:
        print('You entered {skaitlis}. Playing FizzBuzz :)')
        num=float(skaitlis)
        if num < 0:
            num*=-1
            print('Using positive numbers {skaitlis}*-1={num}')
        num=round(num)
        for n in range(1,num+1,1):
            fizz=''
            if n%5==0 or n%7==0: #checking against division by 5, division by 7
                if n%5==0:
                   fizz='Fizz'
                if n%7==0:
                   fizz+='Buzz'
            else:
                fizz=n
            if n <num: # no comma separator at the end
                print(fizz,end=", ")
            else:
                print(fizz, end="")
        break
print()
print('Finish')