while True:
    try:
        skaitlis=float(input('Enter the height of the christmas tree:'))
        num = float(skaitlis)
        if num < 0:
            num *= -1
            print('Using positive numbers {skaitlis}*-1={num}')
        num = round(num)
        x=0
        for star in range(1, num + 1,2):
           c_spaces=num-star
           if star%2==0:
               print(" " * (c_spaces+(star//2)-1), "*" * (star), " " * (c_spaces+(star//2)+1))
           else:
               print(" " * (c_spaces+(star//2)), "*" * (star), " " * (c_spaces+(star//2)))
        break
    except:
        print('number should be given.')
        break
print('Finish!')