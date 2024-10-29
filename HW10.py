#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: HW10
import time
#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
i = 5
while i>= 0:
    print(i)
    time.sleep(.5)
    i-=1
else:
    print("Hello world")

#2. Create a while loop that prints only even numbers
#between 1 and 30.
a = 0
while a<= 30:
    if a % 2 == 0:
        print(a)
    a += 1


#3. Create a while loop that repeats until the user
#inputs the number 0.

b = 0
while b<= 1000:
    print(b)
    time.sleep(.5)
    b += 1
    if input("Enter zero to break code monke.") == "0":
        break

