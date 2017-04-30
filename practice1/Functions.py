import random
import sys
import os

# Defining A Function

def addNumber(fNum,lNum):
    # sumNum is out of scope outside this function
    sumNum = fNum + lNum
    return sumNum

print(addNumber(1,1))

answer = addNumber(2,2)

print(answer)

