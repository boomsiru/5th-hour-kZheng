#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: Scenario 7
import random
#Import all of Scenario 6 here
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

listAverage = 0

def final_average():
    global listAverage
    listAverage = (statList[0]+statList[1]+statList[2]+statList[3]+statList[4]+statList[5])/6 #Calculate the sum of the list by the length of the list here
    return listAverage

final_average()

print(listAverage)