#Name Kevin Zheng
#class 5th hour
#assignment playground


import random


def spin():

       if num <= 100:
              print("U got Doodoo aura!")
       elif num <= 250:
              print("U got grass aura!")
       elif num <= 500:
              print("U got ice aura!")
       elif num <= 700:
              print("U got monke aura!")
       elif num <= 1000:
              print("U got fire aura!")







while input("Press y to spin for an aura ").lower() == "y":
       num = random.randint(1, 1000)
       print(num)
       spin()

else:
       print("stupid monke")











