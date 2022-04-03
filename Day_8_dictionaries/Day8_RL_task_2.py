# Write replace_dict_value (d, bad_val, good_val), which returns a dictionary with changed values
# The parameters of the function are the dictionary d to be processed and the
# values ​​bad_val to be changed to good_val
# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5, 10) ->
# {'a': 10, 'b': 6, 'c': 10}, because 5 was the value to be replaced.

def replace_dict_value (dict_in,bad_val,good_val):

    for key, value in dict_in.copy().items():  # we use copy to go through if we want to delete from original
        if value == bad_val:
            dict_in[key]=good_val
            # careful here we need iterate over copy then or use dictionary comprehension
    return(dict_in)

dict_in={'a': 5, 'b': 6, 'c': 5}

print(f'{dict_in=} => replaced= {replace_dict_value(dict_in,5,10)}')
