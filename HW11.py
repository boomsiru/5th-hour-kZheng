#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: HW11
import time
#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".
i = 0
while i < 100:

    i += 1


    if i % 5 == 0:
        if i % 5 == 0 and i % 3 == 0:
            print("monke ape")
            continue
        print("monke")
        continue


    if i % 3 == 0:
        if i % 5 == 0 and i % 3 == 0:
            print("monke ape")
            continue
        print("ape")
        continue


    print(i)
    time.sleep(0.4)


#Create a while loop that follows the rules of the game.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)