#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#wite sometyhing




def rolld6():
    return random.randint(1,6)
def rolld10():
    return random.randint(1,10)
def rolld20():
    return random.randint(1,20)

class Character:
    def __init__(self, name, attack_power,health, AC, hit ):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        self.AC = AC
        self.hit = hit
    def attack(self, target):
        if target.AC > self.hit:
            self.attack_power = 0


        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

        target.health -= self.attack_power

        if self.health <= 0:
            print( self.name, "is dead")
            exit()


        if target.health <= 0:
            print( target.name, "is dead")
            exit()
        else:
            print(target.name, "is still alive")



Astarion = Character("Astarion", rolld6()+rolld6(), 10, 14, rolld20()+4)
Shadowheart = Character("Shadowheart", rolld10()+2, 10, 14, rolld20()+3)
Gale = Character("Gale", rolld6()+rolld6(), 8,  14, rolld20()+2)
Laezel = Character("Laezel", rolld6()+ 20, 12, 17, rolld20()+6)
CuriousGeorge = Character("Curious George", rolld20() + 100, 100, 20, rolld20()+100)

def perform_attacks(characters, target):
    for character in characters:
        character.attack(target)

perform_attacks([Laezel], CuriousGeorge)


perform_attacks([CuriousGeorge], Laezel)

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)