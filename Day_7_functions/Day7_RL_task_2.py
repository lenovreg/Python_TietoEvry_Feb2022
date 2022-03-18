# 2. Palindrome
# Write the function is_palindrome (text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.
#
# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> Fals
import string

def is_palindrome(teksts:str)->bool:
    opposite_text = teksts[::-1]
    #print(opposite_text)
    opposite_text.strip()
    teksts.strip()
    #print(opposite_text)
    #print(teksts)
    palindrome=False
    for c1, c2 in zip(opposite_text, teksts):  # you can zip many sequences
        if c1 == c2:
            palindrome=True
        else:
            palindrome=False
    return palindrome
res=input("Input some text: ")

print('Text you entered: ', res,end=" ")

print(' is palindrome: ', is_palindrome(res))