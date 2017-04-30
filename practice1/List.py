import random
import sys
import os

'''List'''

car_list = ['Mercedes-Benz','BMW','Ford','Toyota','Chevrolet',
            'Mitsubishi']

print("First Item: ", car_list[0])

# Change Values of first item
car_list[0] = "Hyundai"
print("Changing the value of the First Item to: ", car_list[0])
print("First Item: ", car_list[0])

# print 2st - 3rd Items
print("\n2nd - 3rd Item: ",car_list[1:3])

print("\n" * 5)

other_events = ['Wash Car', 'Pick Up Kids', 'Road Trip']

# Store Two List together in one list
print("Storing 2 list together in one list:")
to_do_list = [other_events,car_list]
print(to_do_list)

# Custom print with the list containing two list
print(to_do_list[0][0],",",to_do_list[0][1],", and go on a", to_do_list[0][2]," with the",(to_do_list[1][1]))

# Append To A List
print("\n")
print("Appending to a list")
car_list.append("Kia")
print(to_do_list)

# Insert To A Specific Index
print("\n")
print("Inserting to a specific index in the list")
print("Inserting\" Bring Me Water in Index 1:")
car_list.insert(1,"Bring Me Water")
print(to_do_list)

# Remove A Specific Index By Value
print("\n")
print("Removing a specific index by value in the list")
print("Removing\" Bring Me Water in Index 1:")
car_list.remove("Bring Me Water")
print(to_do_list)

# Remove A Specific Index
print("\n")
print("Removing a specific index in the list")
print("Removing \" Chevrolet at Index 4:")
del car_list[4]
print(to_do_list)

# Combining list together
print("\n")
print("Combining list together")
to_do_list2 = other_events + car_list
print(to_do_list2)

# Length Of A List
print("\n")
print("Length of to_do_list2: ")
print(len(to_do_list2))

# Max Value Of A List
print("\n")
print("Max Value to_do_list2: ")
print(max(to_do_list2))

# Min Value Of A List
print("\n")
print("Max Value to_do_list2: ")
print(min(to_do_list2))

# Sorting to_do_list2
print("\n")
print("Sorting to_do_list2: ")
to_do_list2.sort()
print(to_do_list2)