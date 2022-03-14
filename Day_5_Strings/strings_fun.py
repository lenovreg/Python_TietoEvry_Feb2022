import string  # this has some extra string constants not required usually
#
# print("My string Fun")  # the text inside is called string literal
# #
food = "kartupelis"
print(type(food))
print(food)
food = "auzu putra"  # here food variable will point to a different string value
print(food)
food = "kartupelis"
print(food)
adjective = "Dārgs "

# String operations
print(adjective + food)
drink = "beer"
print(drink * 5)
# no / no % no -
print("art" in food)  # True
print("music" in food)  # False
print(drink in food)  # False because there is no beer in kartupelis
#
print(len(food))
#
# # # # # # # # # # food
# # # # # # # # # # # Python Slicing syntax
print(food)
print(food[0])  # First letter,why zero index, historic reasons

food_len = len(food)  # how many letters in a string or other collection

print(food_len)  # this is 10 but last letter will be one less because we start at 0
print(food[9])  # letter s,  so index 9 means 10th element
# # print(food[10])  # IndexError: string index out of range because we have 10 symbols,
# # but index 10 would be referring to 11th
print(food[len(food) - 1])  # not pythonic, avoid! Not needed
print(food[-1])  # this is Pythonic way of getting last character of string
print(food[-2])
print(food[2])  # what will be printed ?
print(food[-10])
#print(food[-11])  # IndexError: string index out of range
# #
# # # print(food[555]) # IndexError: string index out of range
# #
# #
# # # # # # # # # # # when slicing we do not include the last index so 5 would be 6th element which we do not include
print(food[0:5], food[:5])  # so index 5(6th element) is not included so we get 1st 5 elements
print(food[0:3], food[:3])  # so index 3(4th element) is not included so we get 1st 3 elements
print(food[:9015])  # when slicing end index can be out of range
print(food[-3000:9015])  # when slicing beginning and end index can be out of range
print(food[-3000:])  # when slicing beginning and end index can be out of range
print(food[:])  # not much point for strings but for other sequences it makes a copy
print(food)
# #
print(food[5:10], food[5:], food[-5:])
food = "Auzu putra ar avenēm un krejumu"
print(food[5:10], food[5:], food[-5:], sep="\n***\n")
print(food[5:-2])  # so we start at the 6th character and we go until the last 2two characters
# # # # # # # # # print(food[400]) # so too much positive will give IndexError
# # # # # # # # # print(food[-320])  # so too much negative will give IndexError
print(food[-320:400]) # we can do this though
print(food[-10:400]) # we can do this though
# #
start = 2  # so to start at 3rd element
end = 6  # and go until but not include 17th element
step = 3
print(food[start:end])
text_len = 10
new_text = food[start:start + text_len]  # so we could generated slice of needed length
print(new_text, len(new_text))
food="Torte Cielavina Rullē"
print(food, len(food))
print(food[5:], food[1:])
print(food)
print(food[0:20:2]) # step can be any whole number
print(food[:20:2])
#
#numbers = "".join(list(range(1,11)))
number_string = "0123456789"
number_string = string.digits  # same as above but guaranteed to be correct even if we change numbers
print(number_string)
print(number_string[start:end])
print(number_string[::2])  # print every second character
# # # print(food[start:end:step])
alphabet = string.ascii_lowercase  # so alphabet variable now points to the same string that string.ascii_lowercase does
my_ascii_letters = string.ascii_letters  # not much point to have such a long name might as well use string.ascii_letters
# for Latvian you will have to make one yourself
print(my_ascii_letters)
print(alphabet)
print(start,end,step)
print(alphabet[start:end:step])
end = 16
print(alphabet[start:end:step])
print(alphabet[end])
# we can find index of what we need
# starting from left side
print(alphabet.index("a"))
print(alphabet.index("s"))
print(alphabet.index("z"))
#
# # print(alphabet.index("V")) # well that will be an error which we could handle with try except block
print(alphabet.find("z"))
print(alphabet.find("V"))
#
# # # # # print(food[::2]) # this would get 2nd character of any strings
print(alphabet[1::2])  # this would get 2nd character of any strings starting with 2nd char
print(number_string[1::2])
# # # # # # # # # # # print(len(food))
# #
# # # # # # # # # # # # reversing a string
print(food)
print(food[::-1])  # so we go backwards
my_reverse_string = food[::-1]  # if I need to save it
print(my_reverse_string)
# #
print(alphabet)
reverse_alphabet = alphabet[::-1]  # so this is common way of reversing some sequence in Python
print(reverse_alphabet)
print(alphabet[15:5:-1])
print(alphabet[15:5:-2])
# #
words = food.split(" ")  # more on that in lists lecture
print(words)
# #
# # # # # # # # # if i need ' inside string then I can use " outside
my_text = "Alice told the rabbit 'go down the hole' and then followed"
print(my_text)
another_text = 'The bottle said "Eat me!" and Alice could not write single quotes'
print(another_text)
#
# # Two approaches for more complex strings
# # notice I also added f before """ to add ability to insert variables
multi_line_string = f"""We can write whatever even go to a
new line
    or use tab
    use single ' and also "
    and \u007b so o \u007d
    un man patīk {food}

    4wt!@#$^&
"""
print(multi_line_string)
#
escaped_string = "text meaning \" and also \' \n \t and of course \\ so on "
print(escaped_string)
food[::-2]
print(food)
print(f"Min ({min(food)}), max({max(food)}), len:{len(food)}")  # min and max use unicode codes
print(ord(" "), ord("e"), ord("ē"))  # Return the Unicode code point for a one-character string
# #
#
another_multi_string = """We have first line actually here
We continue our multiline string
    after tab

last line of our multi
Still a line but now we are done"""
print(another_multi_string)
# # # # # # # # # # # this will not work
# # food[3] = "Z" # will not work
# # # # # # # # # # # # strings are immutable so we need to create new strings
new_food = food.replace('u', 'ū')  # replaces in all places by default count= can specify how many
print(new_food)
new_food = food.replace('u', 'ū', count := 2)  # replaces in all places by default count= can specify how many
print(new_food)
print("X"*len(new_food)) #i can multiple strings with numbers so 20 Xses
print("*"*len(new_food)) #i can multiple strings with numbers so 20 Xses
# #
print("START", food[:3])
print("WILL REPLACE", food[3]) # so we will not keep this one in the new string
print("END", food[4:])
ze_food = food[:3] + "OOO" + food[4:] # so build a new string
print(ze_food)
#
# # f-strings might be more readable
ze_food_2 = f"{food[:3]}O{food[4:]}"
print(ze_food_2)
# # we can overlap slices that is completely fine
print(alphabet[:-3]+"|||"+alphabet[5:])  # we are making a new string from 3 parts here
ze_food_2 = f"{food[:5]}*Jaunais*{food[2:]}" # this will insert new text between old text not losing anything
print(ze_food_2)
food = "mazaiSSSS karTUPelis jaukais"
print(food)
cap_food = food.capitalize() # so first word in capital letters
print(cap_food)
print(food.capitalize())
print(food.title()) # Title Gives Uppercase To Each Word
print(food.upper()) # YELLING
print(food.lower())
print("15004332".isdecimal())
print("15004332badac".isdecimal())  # so isdecimal needs all numbers
# #
print(food.swapcase())
# #
print(food.count("S"))  # this is 4
# turns out strings count is exhaustive meaning it eats up the characters when counting
print(food.count("SS")) # answer should be 2 because we have SSSS
# # print(food.count("SSS")) # answer should be 1 because we have SSS
print(food.count("ai"))
# # # # # # # # # # # print(food.capitalize())
#
# # we can perform multiple methods by chaining them together
print(food.upper().replace("A", "Y")) # i can chain operations on strings
print(food[-5:].upper())  # i can slice and then use some method
# # # # # # # print(food.count('a'))
print(food.index('z')) # z is 3rd element so index is 2
print(food.index('i')) # i is 5th element so index is 4
# # # print(food[4])
# # # # print(food.index("kart")) # so index throws ValueError if not found
# # # print(food.find("kārtis")) # if we do not want ValueError we can use find which returns -1 if not found
# # # print(food.lower().index("kart"))
# # # # # # # print(food.find('z'))
# # # # # # # print(food.find('kart'))
# # # # # # # print(food.lower().find('kart'))
print(food[10:10+4])
# # # # # # # # # # # print(food.index('ž')) # index raises an error
# # # # # # # # print(food.find('ž')) # retursn -1
print(food)
print(food.find('z'))
print(ze_food)
print(ze_food.count("r"))
print(ze_food.find("R"))
print(ze_food.index("R"))
print(ze_food.find("Cielavina"))
print(ze_food.index("Cielavina"))
ze_food.find("ZZ")
# #
# # # print(food)
print("kar" in food) # so in gives us simple Boolean whether substring exists in string
print("kart" in food) # CASE SENsiTIVE so in gives us simple Boolean whether substring exists in string
print("kart" in food.lower()) # so in gives us simple Boolean whether substring exists in string
# # # print("karT" in food) # so in gives us simple Boolean whether substring exists in string
is_found = "kar" in food
print(is_found)
# #
# # we can use a loop to print each character in a string
for c in food:
    print(c, end=":") # so instead of default newline \n i used : as endpoint
print()
print("*"*40)
for c in food[3:8]:
    print(c)
# #
# # # # # # # # # # print(food.index('a'))
#
count = 0
bad_char = "S"
clean_text = ""
for c in food:
    if c == bad_char:
        count += 1
        print("found a bad one", bad_char)
    else:
        clean_text += c # create new string by adding char to old string
print(f"There are {count} {bad_char}s in {food}")
print(f"Cleaned {clean_text=}") # this syntax is starting from Python
print(food.replace("S",""))  #o f course here instead of loop we could have let Python handle this
# #
# # # # # # # # # # # food, clean_text
# #
print(zip(food,clean_text))
fresh_text = ""
for c1, c2 in zip(food, clean_text):  # you can zip many sequences
    if c1 == c2:
        fresh_text += c1  # also c2 would work # not great for long texts
    else:  # mismatch
        fresh_text += "_"
print(fresh_text)
#
print("Going to loop through 2 strings at once until one runs out")
print("First string", alphabet)
print("Second string", number_string)
result = ""
for letter, number in zip(alphabet, number_string):
    print(letter, "and", number)
    result += f"Letter {number} is {letter}\n"  #not the most efficient for large strings
print("All done with looping through two strings")
print(result)
# # so above loop ends as soon as one of the sequences run out
#
#
# # # # # # # # # isArtFound = "art" in food
# # # # # # # # # print(isArtFound)
# #
print("Valdis" < "Voldemars")  # because 'a' , 'o' in Unicode table
print("Valdis" < "Voldis")  # because 'a' , 'o' in Unicode table
print(len("Valdis") < len("Voldemars"))  # by length
# #
# # # # # # # # # # # print("Alice said 'Run rabbit run!' and drunk something")
# # # # # # # # # # # print("When we need both quotes \" \\ and also ' \n\n new lines ")
# # # # # # # # # # # print(""" I can write whatever here
# # # # # # # # # # # even new lines
# # # # # # # # # # #             with tabs
# # # # # # # # # # #              ' " " " '
# # # # # # # # # # # """)
# # # # # # # # # # # print(food.upper())
# # # print(food.isalpha())
big_food = food + " banana"
print(big_food)
print(big_food.find("an"))
print(big_food.rfind("an")) # start searching from the right side
#
city = "    Rīga     "
print(city.strip())  # clean up both sides
print(city.rstrip())
print(city.lstrip())  # we still have whitespace after right side
print(city)  # city is still dirty
clean_city = city.strip()
print(clean_city)
print(big_food)
print(big_food.find("a"))
print(len(big_food))
print(big_food.rfind("a"))
sentence = "A quick brown fox run over a sleeping dog"
words = sentence.split()
print(words)
