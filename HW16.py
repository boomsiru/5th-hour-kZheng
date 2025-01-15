#Name:Kevin Zheng
#Class: 5th Hour
#Assignment: HW16
import random
import time


#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def Jaken():
    while True:

        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

        # Take the input from user
        choice = int(input("Enter your choice: "))

        # Looping until user enters valid input
        while choice > 3 or choice < 1:
            choice = int(input('Enter a valid choice please ☺: '))

        # Initialize value of choice_name variable corresponding to the choice value
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'

        # Print user choice

        print('User choice is:', choice_name)
        time.sleep(.5)
        print("Now it's Computer's Turn...")
        time.sleep(.7)
        # Computer chooses randomly any number among 1, 2, and 3
        comp_choice = random.randint(1, 3)

        # Initialize value of comp_choice_name variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'

        print("Computer choice is:", comp_choice_name)
        time.sleep(.5)
        print(choice_name, 'vs', comp_choice_name)


        # Determine the winner
        if choice == comp_choice:
            result = "DRAW"
        elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
            result = 'Paper'
        elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
            result = 'Rock'
        elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
            result = 'Scissors'

        # Print the result
        if result == "DRAW":
            print("<== It's a tie! ==>")
        elif result == choice_name:
            print("<== User wins! ==>")
        else:
            print("<== Computer wins! ==>")

        # Ask if the user wants to play again
        loop()

    # After coming out of the while loop, print thanks for playing


#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def loop():
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        print("Thanks for playing!")
        exit()

Jaken()

