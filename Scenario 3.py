#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: Scenario 3
import math

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4



#Party Dictionary Goes Here


import math
import random
from tkinter import mainloop






def rolld6():
    return random.randint(1,6)
def rolld10():
    return random.randint(1,10)
def rolld20():
    return random.randint(1,20)

class Character:
    def __init__(self, name, attack_power,health, AC ):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        self.AC = AC
    def attack(self, target):
        attkdmg = self.attack_power - target.AC
        vhealth = attkdmg - self.health
        if attkdmg <= 0:
            attkdmg = 0
        print(f"{self.name} attacks {target.name} for {attkdmg} damage!")
        if CuriousGeorge vhealth <= 0:
            print({self.name}, "is dead")
        if Laezel vhealth <= 0:
            print({self.name}, "is dead")


Astarion = Character("Astarion", rolld6()+rolld6(), 10, 14)
Shadowheart = Character("Shadowheart", rolld10()+2, 10, 14)
Gale = Character("Gale", rolld6()+rolld6(), 8,  14)
Laezel = Character("Laezel", rolld6()+rolld6(), 12, 17)
CuriousGeorge = Character("Curious George", 100, 100, 20)

def perform_attacks(characters, target):
    for character in characters:
        character.attack(target)

partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damagemod" : 6,
        "dmgroll": rolld6() + rolld6() + 3
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damagemod" : 3,
        "dmgroll": rolld6() + 2
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damagemod" : 5,
        "dmgroll": rolld6() + 2
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damagemod" : 4,
        "dmgroll": rolld10()
    }
}


#Enemy Dictionary Goes Here
MonkeyDict = {
    "Diddy Kong": {
        "Health" : 10,
        "Damagemod" : 2,
        "AC" : 10,
        "dmgroll": rolld6() + 1
    },
    "Dixie Kong": {
        "Health" : 10,
        "Damagemod" : 3,
        "AC" : 12,
        "dmgroll": rolld6() + 1
    },
    "Donkey Kong": {
        "Health" : 20,
        "Damagemod" : 10,
        "AC" : 14,
        "dmgroll": rolld10() + 3
    },
    "King Kong" : {
        "Health" : 40,
        "Damagemod" : 20,
        "AC" : 15,
        "dmgroll":  rolld10() + 5

    },
    "Curious George" : {
        "Health" : 100,
        "Damagemod" : 100,
        "AC" : 17,
        "dmgroll" : rolld20() + 10
    }
}



#Combat Code Goes Here

perform_attacks([Laezel], CuriousGeorge)


perform_attacks([CuriousGeorge], Laezel)



