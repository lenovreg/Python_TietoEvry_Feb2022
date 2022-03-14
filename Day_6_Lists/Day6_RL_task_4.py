while True:
    try:
        res=int(input('Please enter any positive number or any other character to quit:'))
        num = res
        primary_count=0
        primary_list=[]
        for n in range(num,num+100):
            skaits=0
            for i in range(1,n+1):
                if n%i==0:
                   skaits+=1
            if skaits==2:
                primary_list.append(n)
                primary_count+=1
            if primary_count>=20:
                break
        print(f'primary numbers list starting with {num} is:  {primary_list}')
    except:
        print('Stopping.')
        break
print('Finish!')