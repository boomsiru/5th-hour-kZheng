#Name: Kevin zheng
#Class: 5th Hour
#Assigment: Scenario 6
import random

#After an extended leave, the team lead for the RPG developer is back, and he wants to continue the project.
#He wants to prototype the character creation model but first needs something that rolls stats for the characters.
#He wants you to make a function that rolls 4 six-sided dice (d6), sorts them from highest to lowest, and then adds the
#highest 3 together. He then wants you to add that result to a list outside the function. He wants you to run that function
#5 more times (six times total) and print all six stats.
statList = []
def roll():
    for i in range (0,6):
        stat1 = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
        print(stat1)
        stat1.sort(reverse=True)
        stats = stat1[0]+stat1[1]+stat1[2]
        print(stats)
        statList.append(stats)
roll()
print(statList)

#Once that is done, to ensure that the average of the statblock is fair (somewhere roughly between 12-13), he wants you
#to plug it into a calculator (Scenario 7) and print the average.