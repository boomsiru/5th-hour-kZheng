#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: HW20
from logging import raiseExceptions

#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World!")
#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
y = int(input("plese print number"))
try:
    print(100/y)
except:
    print("cannot divide by 0")

#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.

try:
    n = int(input(f"plese print number"))
except ValueError: print("not a number")



#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
j = 5

while j <= 5:
    print(j)
    j-=1
    if j < 0:
        raise Exception ("cannot go below zero")

