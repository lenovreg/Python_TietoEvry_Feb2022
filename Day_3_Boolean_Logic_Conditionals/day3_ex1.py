# Exercise 1

temperature = float(input("What's your temperature?"))
if temperature < 35:
    print("not too cold")
elif 35 <= temperature <= 37: # so  inclusive same as 35 <= temperature and temperature <= 37:
    print("all right")
else:
    print("possible fever")
