while True:
    try:
        res=int(input('Please enter any positive number or any other character to quit:'))
        if res>0:
            num = res
            ir_pirmskaitlis=False
            skaits=0
            if num > 0:
                for i in range(1,num+1):
                    if num%i==0:
                       skaits+=1
                if skaits==2:
                    print(f'Number you have entered {res} is primary number.')
                else:
                    print(f'Number you have entered {res} is not a primary number.')
            continue
    except:
        print('number should be given.')
        break
print('Finish!')