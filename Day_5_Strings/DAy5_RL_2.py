import string
# Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.
# Example:
# First input: Kartupeļu lauks -> ********* *****
# Second input: a -> *a****** *a***
user1_text = input("Put some text:")
asterix="*"
asterix_text=""
for c in user1_text:
    if c==" ":
        asterix_text+=c
    else:
        asterix_text+=asterix
print(asterix_text)
user2_c = input("Input some symbol:")
for n, c in enumerate(user1_text):
    pos=user1_text.find(user2_c,n)
    if pos >= 0:
        asterix_text=asterix_text[:pos]+user2_c+asterix_text[pos+1:]

print(asterix_text)
