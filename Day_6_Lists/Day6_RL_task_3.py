# Reversed words
# The user enters a sentence.
# We output all the words of the sentence in reverse form. - not the whole text reversed!!
#
# Example
# Alus kauss mans -> Sula ssuak snam
# PS Split and join operations could be useful here.

res=input('Enter some sentence (text): ')
my_text=res.split()
my_str1=" ".join(my_text)
print('You entered text: ',my_str1)
new_text=[]
for t in my_text:
    my_str="".join(t)
    new_text.append(my_str[::-1])
new_str=" ".join(new_text)
print("Text in revered form: ", new_str)