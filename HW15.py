#Name:Kevin Zheng
#Class: 5th Hour
#Assignment: HW15
import random
#1. Create a def function that prints out "Hello World!"
def monke():
    print("hello monke")
#2. Create a def function that calculates the average of three numbers.
def AvgmMonke(a,b,c):
    avg = a+b+c / 3
    print(avg)

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def Monke_list(*monkey):
    print("The 3rd monke is", monkey[2])



#4. Create a def function that loops from 1 to the number put in the argument.
def monkeloop(t):

    for x in range(1,t+1):
        print(x)


#5. Call all of the functions created in 1 - 4 with relevant arguments.

monke()
AvgmMonke(a = random.randint(1,3), b = random.randint(1, 3), c = random.randint(1, 3) )
Monke_list("Ape", "Chimp", "monke", "Kong", "fraud")
monkeloop(t = int(input("please enter number")))