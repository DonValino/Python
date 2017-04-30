import random
import sys
import os

# if else elif == != > >= <=

age = 21

if age >= 21 :
    print("You Are Old Enough To Drive A Bus")
elif age >= 16 :
    print("You Are Old Enough To Drive A Car or Motorcycle")
else :
    print("You Are Not Old Enough To Drive")

# Combining conditions with logical operators
# Logical operators: and, or, not
print("\n")
if((age >= 1) and (age <= 18)) :
    print("You are aged between 1 and 18")
elif((age == 21) or (age >= 65)) :
    print("You are a senior of working age")
elif not (age == 30) :
    print("You are not yet considered a fully growned adult")
else :
    print("Don't know")