import random
import sys
import os

''' Unlike List, we are not going to be able to change a tuple
    after it has been created'''
# Use a Tuple if you want data that cannot be easily changed

pi_tuple = (3,1,4,1,5,9)

# If we want to make changes to values inside a Tuple:
# Convert a tuple into a list
new_tuple = list(pi_tuple)
# Make Your changes
new_tuple[0] = 1
# Convert Back to tuple
new_list = tuple(new_tuple)

# After Changes
print("After Changes: ", end="")
print(new_list[0])

print("\n")
print("Length: ")
print(len(new_list))
print("Min: ")
print(min(new_list))
print("Max: ")
print(max(new_list))

