# The user enters a name.
#
# You print user name in reverse (should begin with capital letter) then extra text: ",a thorough mess is it not ",
# then the first name of the user name then "?"
#
# Example:
#
# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?
name_in_reverse=""
your_name=input("Please, enter your name:")
for c in your_name[::-1].lower():
    name_in_reverse+=c
print(f'{name_in_reverse.title()}, a thorough mess is it not {name_in_reverse[-1:].upper()}?')