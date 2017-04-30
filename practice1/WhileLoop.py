import random
import sys
import os

# Looping

# Generate Random Numbers from 0-99
print("Generating a random number")
random_num = random.randrange(0,100)

# Loop While 15 is not the selected value
while(random_num != 15):
    # Print if not 15
    print(random_num)
    # Continue generating new number if value not 15
    print("Generating a random number")
    random_num = random.randrange(0,100)

print("\n")

print("Value is now: " , random_num)

# Creating an iterator
print("\n")
print("Creating An Iterator:")
i = 10

while(i <= 20):
    # Printing All The Even Numbers
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        # Exit The while loop
        break
    else:
        i += 1
        # Jump to the top of the while loop
        continue

    # i is an even number so increment i by 1
    i +=1