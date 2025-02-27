#Name Kevin Zheng
#class 5th hour
#assignment playground

import time
import random
crazybiome = 0
doodoo = 0
grass = 0
ice = 0
monke = 0
fire = 0
inventory = []
#make ui better
def spin():
       global doodoo
       global grass
       global ice
       global monke
       global fire
       if num <= 100:
              print("U got Doodoo aura!")
              inventory.append(doodoo)
              doodoo+=1


       elif num <= 250:
              print("U got grass aura!")
              inventory.append(grass)
              grass+=1

       elif num <= 500:
              print("U got ice aura!")
              inventory.append(ice)
              ice+=1

       elif num <= 700:
              print("U got monke aura!")
              inventory.append(monke)
              monke+=1

       elif num <= 1000:
              print("U got fire aura!")
              inventory.append(fire)
              fire+=1






while input("Press y to spin for an aura ").lower() == "y":
       num = random.randint(1, 1000)
       if crazybiome == 1:
              num = random.randint(1,2000)
       print(num)
       spin()
       print(inventory)
       time.sleep(.5)

else:
       print("stupid monke")
       
       











