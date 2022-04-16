# 3. Is there a pangram?
# Write a function is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz')
# that returns True when the text parameter contains all the letters passed in an alphabet.
# We return False otherwise
# pangram - sentence, word string containing all letters of the alphabet - https://en.wikipedia.org/wiki/Pangram
# We ignore spaces and believe that uppercase is as valid as lowercase, i. here A and a -> a
# print(is_pangram("The five boxing wizards jump quickly")) -> True
# print(is_pangram("Not a pangram")) -> False
#
# Bonus: test it also on Latvian alphabet:
# a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
# print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alphabet=a_lv)) -> True
import string

def is_pangram(text, alphabet):
    text=set("".join(text.split()))
    my_set={str(c).lower() for c in text if (str(c).lower() not in string.punctuation )}
    return my_set.issuperset(set(alphabet))

alphabet=set(string.ascii_lowercase)
#print(alphabet)
teksts='The five boxing wizards jump quickly'
print(f'{teksts} is pangram {is_pangram(teksts,alphabet)}')
a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
teksts='Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!'
print(f'{teksts} is pangram {is_pangram(teksts,a_lv)}')
teksts="Not a pangram"
print(f'{teksts} is pangram {is_pangram(teksts,alphabet)}')