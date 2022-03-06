# #1. Health check
# # Ask user for their temperature.
# # If the user enters below 35, then output "not too cold"
# # If 35 to 37 (inclusive), output "all right"
# # If the temperature  over 37, then output  "possible fever"
#
user_temp = float(input('What is your temperature?'))
if user_temp < 35:
    print('not too cold?')
elif user_temp >= 35 and user_temp <= 37:
    print('all right')
else: # temperature over 37
    print('possible fever')
