# Write a program for text conversion
# Save user input
# Print the entered text without changes
# Exception: if the words in the input are not .... bad, then the output is not ...  bad section must be changed to is good
#
# Examples:
# The weather is not bad -> The weather is good
# The car is not new -> The car is not new
# This cottage cheese is not so bad -> This cottage cheese is good
#
# Hints:
# Find (or index, or even rfind) will probably come in handy, as may an operator. Also slice syntax will be useful.
# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?

user_text=input("Enter some text: ")
cnt_not=0
cnt_bad=0
for n,c2 in enumerate(user_text):
    pos1=user_text.lower().rfind("not",n)
    pos2=user_text.lower().rfind("bad",n)
    if pos1 !=-1:
        cnt_not+=1
    if pos2 !=-1:
        cnt_bad+=1
new_text=user_text.replace("not","is",cnt_not).replace("bad","good",cnt_bad).replace("is is","is")
print(new_text)