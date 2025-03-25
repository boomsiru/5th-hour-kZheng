#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: HW24

import random, time



#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class character:
    def __init__(self, health, damage, speed, maxhealth):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.maxhealth = maxhealth
    def loop(self):
        for x in range (10):
            self.health -= random.randint(1,6)
            print(f"new hp is ",self.health)
            time.sleep(.3)
    def heal(self):
        if self.maxhealth > self.health:
            self.health += 30
            if self.maxhealth < self.health:
                self.health = self.maxhealth

#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
healer = character(60,10,30, 60)
warrior = character (100,20,30, 100)
thief = character (50,30,40, 50)
mage = character (45,35,25, 45)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
person = random.randint(1,4)
if person == 1:
    warrior.loop()
elif person == 2:
    healer.loop()
elif person == 3:
    thief.loop()
elif person == 4:
    mage.loop()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
if warrior.maxhealth > warrior.health:
    warrior.heal()
    print("warrior hp is ", warrior.health)
elif healer.maxhealth > healer.health:
    healer.heal()
    print("healer hp is ", healer.health)
elif mage.maxhealth > mage.health:
    mage.heal()
    print("mage hp is ", mage.health)
elif thief.maxhealth > thief.health:
    thief.heal()
    print("thief hp is ", thief.health)
