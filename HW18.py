#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
from os import remove


def hello():
    print("Hello monkeys")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["red", "blue", "green", "brown", "black"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def pull():
    bean = random.choice(beanBag)
    print(bean)
    beanBag.remove(bean)
    if beanBag:
         print("bean bag has beans")
    elif not beanBag:
        print("bean bag does not have beans")
        exit()
    loop()

#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def loop():
    the = input("press y if bean again and n if not")
    if the  == "y":
        pull()

    elif the == "n":
        exit()

#5. Call the #3 function at the bottom.
pull()