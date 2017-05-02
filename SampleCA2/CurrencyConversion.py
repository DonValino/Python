import random
from functools import reduce

# Method To Convert Euro To Dollars
def ConvertToDollars(euro):
    return euro * 1.0931

# Method to Convert Dollars To Euro
def ConvertToEuro(dollars):
    return dollars * 0.9148

print("100 Euro in Dollars: $", str(round(ConvertToDollars(100),2)))
print("100 Dollars in Euro: €", str(round(ConvertToEuro(100),2)))

# High Order Function Which Takes As Parameter a function and a value to be converted
def ConvertCurrency(method,money):
    return method(money)

print("\nHigh Order Function Conversion:")
print("100 Euro in Dollars: $", str(round(ConvertCurrency(ConvertToDollars,100),2)))

# List of 5 random money in range 100 - 1000
print("\nGenerating 5 random dollars:")
dollars = [random.uniform(100,1000) for _ in range(5)]

print("$: ",str(dollars))

# Calculate Average Dollar Value using reduce
averageDollarValue = reduce(lambda a,b: a + b, dollars ) / len(dollars)
print("Average Dollar Value: $", str(round(averageDollarValue,2)))

# Minimum Dollar Value using reduce
minDollarValue = reduce(lambda minimum,current: current if current < minimum else minimum, dollars)
print("Minimum Dollar Value: $" , str(round(minDollarValue,2)))

# Maximum Dollar Value using reduce
maxDollarValue = reduce(lambda maximum,current: current if current > maximum else maximum, dollars)
print("Maximum Dollar Value: $" , str(round(maxDollarValue,2)))

# Map To Convert list to Euro values using high-order function created earlier
euros = list(map(lambda x:ConvertCurrency(ConvertToEuro,x), dollars))
print("\nDollars converted To Euros: \n€" + str(euros))

# Getting The First Euro Value
print("\nGetting The First Euro Value: €", str(round(euros[0],2)))