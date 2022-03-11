while True:
    try:
        res=input('Please enter any positive number or q to quit:')
        if res[0].lower().isalpha()=='q':
            print('Fininsh testing primary numbers')
            break
        else:
            num = int(res)
            ir_pirmskaitlis=False
            skaits=0
            if num > 0:
                for i in range(1,num+1):
                    if num%i==0:
                       skaits+=1
                if skaits==2:
                    print(f'Number you have entered {skaitlis} is primary number.')
                else:
                    print(f'Number you have entered {skaitlis} is not a primary number.')
            continue
    except:
        print('number should be given.')
        break
print('Finish!')