# 2. Exercise - Room volume
#
# Ask user to input 3 numbers - width, length, height
# Find the volume of the room
# PS Think about units and what is the most appropriate data type for this

room_hight = float(input('Please enter room hight (in meters):'))
room_length = float(input('Please enter room length (in meters):'))
room_width = float(input('Please enter room width (in meters):'))

room_volume = room_length * room_width * room_width
print(f'Room size is: {round(room_volume,2)} m\u00B3')