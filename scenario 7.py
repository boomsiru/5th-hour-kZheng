#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: Scenario 7
import random
#Import all of Scenario 6 here

from Secenario6 import roll, StatList








listAverage = 0

def final_average():
    global listAverage
    listAverage = sum(StatList)/len(StatList)#Calculate the sum of the list by the length of the list here
    return listAverage

final_average()

print(listAverage)
