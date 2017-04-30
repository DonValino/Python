import random
import sys
import os

# Looping

#Printing the defined range
print("Printing the defined range:")
for x in range(0,10) :
    print(x, ' ',  end="")

print("\n")

car_list = ['Mercedes-Benz','BMW','Ford','Toyota','Chevrolet',
            'Mitsubishi']

#Printing the car list with for loop
print("Printing the car list with for loop:")
for y in car_list:
    print(y)

#Printing based on set values
print("\n")
print("Printing based on set values:")
for x in [2,4,6,8,10]:
    print(x)

# List Inside A List
print("\n")
print("List Inside A List:")
num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0, 3):
        print(num_list[x][y])