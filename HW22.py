#Name:Kevin Zheng
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class items:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight

    def Timescost(self):
        self.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
bananna = items(10,2,2)
apple = items(20,3,1)
grapes = items(30,4,4)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"The cost of items is ,{apple.stock,bananna.stock,grapes.stock} apple has {apple.stock} in stock")
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
apple.Timescost()
print(f"apple costs {apple.cost} dollars")

#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
grapes.stock = 7
print(f"there is {grapes.stock} grapes left ")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del apple
try:
    print(apple.weight)
except:
    print("there is no apple monke")