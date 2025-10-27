'''Project 2: Simple Calculator
Ask the user for two numbers and an operation (+, -, *, /)
Use functions for each operation
Display the result
Concepts used: functions, conditionals, input/output'''

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

while True:
    print("----Simple Calculator----")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting... Thank you for using the calculator!")
        break

    if choice in [1, 2, 3, 4]:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))

        if choice == 1:
            print("Sum is:", add(a, b))
        elif choice == 2:
            print("Subtraction is:", sub(a, b))
        elif choice == 3:
            print("Multiplication is:", mul(a, b))
        elif choice == 4:
            print("Division is:", div(a, b))
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")



