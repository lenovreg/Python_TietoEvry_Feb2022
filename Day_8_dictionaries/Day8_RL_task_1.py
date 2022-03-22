# 1. What's the frequency?
# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single letter applications.
# get_char_count ("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, '': 1}
# # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included
#  There may also be a solution with Counter from standard Python library but this is definitely not necessary, although it is very elegant smile
#

def get_char_count(tt:str):
    my_dict={}
    n=0
    tt=tt.strip()
    for c in tt:
        if c in my_dict:
            my_dict[c] += 1
        else:
            my_dict[c] = 1
    return my_dict
res=input("Input some text: ")
print(get_char_count(res))
