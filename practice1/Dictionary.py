import random
import sys
import os

'''Dictionary / Maps: Made up of values that you can't
    join dictionaries together like you can with list with
    + on it'''

# Creating a Dictionary
                  #Secret     Identity
super_villains = {'Fiddler': 'Isaac Bowin',
                  'Captain Cold': 'Leonard Snart'}

# Get The secret identity
print("Getting The Secret Identity: ")
print(super_villains['Captain Cold'])

# Deleting an entry
del super_villains['Fiddler']
print("\n")
print("Deleting Fidler: ")
print(super_villains)

# Change the secret identity
print("\n")
print("Changing Captain Cold: ")
super_villains['Captain Cold'] = "Huiston"
print(super_villains)

# Length
print("\n")
print("Length: ")
print(len(super_villains))

# Using The Get Method
print("\n")
print("Using the \"get Method: ")
print(super_villains.get("Captain Cold"))

# Get the list of keys
print("\n")
print("Getting the list of keys: ")
print(super_villains.keys())

# Get the list of keys
print("\n")
print("Getting the list of values: ")
print(super_villains.values())


