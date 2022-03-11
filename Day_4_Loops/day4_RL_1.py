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