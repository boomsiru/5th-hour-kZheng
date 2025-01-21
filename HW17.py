#Name:Kevin Zheng
#Class: 5th Hour
#Assignment: HW17


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hello():
    print("Hello monkes")
#2. Create two empty integer variables named "heads" and "tails"
head = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coinfilp():
    for amount in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            global head
            head += 1
        else:
            global tails
            tails += 1


#4. Call the "Hello world" and "Coin Flip" functions here
hello()
coinfilp()
#5. Print the final result of heads and tails here
print(head)
print(tails)