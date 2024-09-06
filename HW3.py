#Name Kevin
#Class 5th
#assignment HW3

print("hello world")
monkeList = ["Monke1" , "Monke2" , "Monke3" , "Monke4" , "Monke5"]
monkeList.append(input("please enter monke"))
print(f"{monkeList[3]}")

NumList = [ 1, 4, 3, 4,]
NumList.insert(1, 1)
print(NumList)
NumList.sort()
sum = NumList[0] + NumList[1] + NumList[2]
print(sum)

print("Hello, please enter a name")
input()
print("Trick question u are a Monke")

x = int(input("Now type a number: "))
if x > 0:
    print("You are a positive monke")
elif x < 0:
    print("You are a negative monke")
else:
    print("You stupid monke")
y = int(input("Type another number: "))
if y > 0:
    print("You are a positive monke again")
elif y < 0:
    print("You are a negative monke again")
else:
    print("You are a goober")

sum = (x) + (y)

print("The sum is:", sum, "stupid monke")
