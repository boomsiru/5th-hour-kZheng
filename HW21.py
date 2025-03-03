#Name:Kevin Zheng
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
sportsfr = {
    "sport1":{
    "sport" : "football",
    "players": 53,
    "ball" : True
},
    "sport2":{
    "sport" : "basketball",
    "players": 5,
    "ball" : True
    },
"sport3":{
    "sport" : "golf",
    "players": 1,
    "ball" : True
}
}
#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def adding(a,b,c):
    print("total is",a+b+c)

#3. Call the function with arguments here\
adding(sportsfr["sport1"]["players"],sportsfr["sport2"]["players"],sportsfr["sport3"]["players"])