def add(x,y):
    return x+y

def subtract (x,y):
    return x-y

def multiply (x,y):
    return x*y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


while True:
    choice = input("Enter choice 1/2/3/4:")

    if choice in ('1', '2', '3', '4'):
        try:
            num1= float(input("Enter first number:"))
            num2= float(input("Enter second number:"))
        except ValueError:
            print("Stupid monkey, enter an actual number")
            continue


    if  choice  == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))


    elif choice == '4':

        result = divide(num1, num2)

        if isinstance(result, str):  # check if the result is an error message

            print(result)

        else:

            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please select a valid operation.")

    nextcalc = input("Do you want to do another calculation? (yes/no): ").lower()
    if  nextcalc == "no":
        break
    elif nextcalc != "yes":
        print("Invalid input. Please enter 'yes' or 'no'.")

    else:
        print("ok monke")


