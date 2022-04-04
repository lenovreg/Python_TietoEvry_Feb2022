#Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.
#get_common_elements (seq1, seq2, seq3)
#Example:
#get_common_elements ("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element
## remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)
#2. b For those with some experience
#BONUS:  make a function that can handle an arbitrary number of input sequences
def convert_tuple_to_set(my_tuple):
    my_list=[]
    if type(my_tuple)==tuple:
        for item in my_tuple:
            my_list+="".join(item)
        my_set=set(my_list)
    else:
        my_set=set(my_tuple)
    return my_set
def get_common_elements(seq1, seq2, seq3):
    common_seq=set(seq1)&set(seq2)&set(seq3)
    return tuple(common_seq)
seq1="abc"
seq2=['a', 'b']
seq3=('b', 'c')
# seq1=('kaut kas','briniksigs','1')
# seq2=['a','b', 'b']
# seq3=('b', 'c','3','4')
print(f'{seq1=},{type(seq1)}; {seq2=},{type(seq2)}; {seq3=},{type(seq3)}')
print (f' common elements for seq1 & seq2 & seq3 are  {get_common_elements (convert_tuple_to_set(seq1), convert_tuple_to_set(seq2), convert_tuple_to_set(seq3))}')