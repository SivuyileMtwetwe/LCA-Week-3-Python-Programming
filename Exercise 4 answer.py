# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple", "orange", "banana", "grape", "lemon","mango","strawberry", "naartjies"]
# TODO: Use a for loop to print each fruit in the list
for i in fruits:
    print(i)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
j = 6

while j>1:
    j-=1
    print(j)
    

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1,11):
    print(i**2)
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colours = ["red","pink","yellow", "brown","blue","grey"]
# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
    random_colours = random.choice(colours)

    print(random_colours)
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations

# TODO: Use a while loop to create a simple calculator
def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter operation number (1/2/3/4) or 'q' to quit: ")
        
        if choice == 'q':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please try again.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", math_operations.add(num1, num2))
        elif choice == '2':
            print("Result:", math_operations.subtract(num1, num2))
        elif choice == '3':
            print("Result:", math_operations.multiply(num1, num2))
        elif choice == '4':
            print("Result:", math_operations.divide(num1, num2))

if __name__ == "__main__":
    calculator()