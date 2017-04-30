import random
from functools import reduce

# Method to convert Celsius temperature value to Fahrenheit
def ConvertToFahrenheit(temp):
    return ((temp * 9) / 5) + 32

# Method to convert Fahrenheit temperature value to Celsius
def ConvertToCelsius(temp):
    return ((temp - 32) * 5) / 9

print("Fahrenheit: ",str(round(ConvertToFahrenheit(0), 2)))
print("Celsius: ",str(round(ConvertToCelsius(0), 2)))

# High-order function which takes as parameter a function and a value
# to be converted
def ConvertTemp(method, temp):
    return method(temp)

print("Fahrenheit: ",str(round(ConvertTemp(ConvertToFahrenheit,0), 2)))

# List of 5 random values in range 1.0 - 25.0
print("\n")
print("Generating 5 random celsius temperature:")
celcius_random_temp = [random.uniform(1.0,25.0) for _ in range(5)]

print("Celsius: ",str(celcius_random_temp))

# Calculate Average Temperature using reduce
averageTemp = reduce(lambda a,b:a + b, celcius_random_temp) / len(celcius_random_temp)
print("Average temperatue: " , str(round(averageTemp,2)))

# Minimum Temperature using reduce
minTemp = reduce(lambda minimum,current : current if current < minimum else minimum, celcius_random_temp)
print("Minimum temperatue: " , str(round(minTemp,2)))

# Maximum Temperature using reduce
maxTemp = reduce(lambda maximum, current: current if current > maximum else maximum, celcius_random_temp)
print("Maximum temperatue: " , str(round(maxTemp,2)))

# Map To Convert list to Fahrenheit values to Celsius using high-order function created earlier
fahrenheit_Temperatures = list(map(lambda x:ConvertTemp(ConvertToFahrenheit,x), celcius_random_temp))
print("Fahrenheit: " + str(fahrenheit_Temperatures))

# Getting The First Fahrenheit Temperature
print("Getting The First Fahrenheit Temperature: ", str(round(fahrenheit_Temperatures[0],2)))