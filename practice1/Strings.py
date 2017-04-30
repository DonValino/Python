import random
import sys
import os

long_string = "Its My Life - Bon Jovi"

# Print Out the first 4 characters
print("Print Out the first 4 characters:")
print(long_string[0:4])

# Print The Last 5 characters
print("\n")
print("Print The Last 5 characters:")
print(long_string[-5:])

# Print Everything up to the last 5 characters
print("\n")
print("Print Everything up to the last 5 characters:")
print(long_string[:-5])

# Join 2 strings together
print("\n")
print("Join 2 strings together:")
print(long_string[:4] + "not my life")

# Print method string parameters
print("\n")
print("Print method string parameters:")
print("%c us my %s letter and my number %d number is %.5f" %
      ('X','favorite',1,.14)) # %.5f - print in 5 decimal places


# Capitalize the first word of the string
print("\n")
print("Capitalize the first word of the string:")
print(long_string.capitalize())

# Find a word in a string
print("\n")
print("Find a word in a string:")
print("Index: ", long_string.find("Life"))

# Check That all strings are letters
print("\n")
print("Check That all strings are letters:")
print(long_string.isalpha())

# Check That all strings are numbers
print("\n")
print("Check That all strings are letters:")
print(long_string.isalnum())

# Length Of String
print("\n")
print("Length Of String:")
print(len(long_string))

# Replace A Word in a string
print("\n")
print("Replace A Word in a string:")
print(long_string.replace("Life", "Cookie"))

# Strip White Spaces
print("\n")
print("Strip White Spaces:")
print(long_string.strip())

# Split string into a list
print("\n")
print("Split string into a list:")
quote_list = long_string.split(" ")
print(quote_list)
