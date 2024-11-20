#Name:Kevin Zheng
#Class: 5th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
ratings = 0
players = 0
sum = 0
players = int(input("please enter number of players"))

if 1> players:
    print("monke")
    exit()




for q in range (0, players):
    while True:
        ratings = int(input("please give rating of 1-5"))
        if 1 > ratings or ratings > 5:
            print("monke")
            continue
        else:
            sum += ratings
            break

print(sum/players)





