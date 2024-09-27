#Name:Kevin
#Class: 5th Hour
#Assignment: HW5

#1. Print "Hello World!"

#2. Create a list that contains 3 integers

#3. Create an if statement that prints out whichever of the three numbers is the highest
print("Hello World!")

num1list = [4,1,2,]


if num1list[2] > num1list[0] and num1list[2] > num1list[1]:
    print(num1list[2], "monkes in a cage")
elif num1list[0] > num1list[1] and num1list[0] > num1list[2]:
    print(num1list[0], "monkes in a cage")
elif num1list[2] > num1list[1] and num1list[2] > num1list[0]:
    print(num1list[2], "monkes in a cage")

else: print("stupid monke")
