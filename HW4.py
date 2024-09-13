#Name: Kevin Zheng
#Class: 5th
#assignment: HW4


print("hello world")
MonkeDict = {
    "type of monkey(etc)" : "gorilla",
    "fur color" : "black",
    "number of eyes" : [2,2,2]
}
print(MonkeDict["number of eyes"][1])
MonkeDict.update({"tail" : False})


print(MonkeDict)
MonkeDict.clear()
print(MonkeDict)

ClassDict = {
    "Student1" : {
        "Name" : "Zach",
        "Grade" : 12,
        "esports" : False
    },
    "Student2" : {
        "Name" : "Chaysen",
        "Grade" : 11,
        "esports" : False
    },
    "Student3" : {
        "Name" : "Sam",
        "Grade" : 9,
        "esports" : False
    }
}
print(ClassDict["Student1"]["Name"],ClassDict["Student2"]["Name"],ClassDict["Student3"]["Name"])






