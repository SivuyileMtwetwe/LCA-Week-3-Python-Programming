# Question 1: Variable Assignment and String Manipulation

# Ask the user for their name and store it in a variable
name = input("Enter your name: ")
# Ask the user for their age and store it in a variable
age = int(input("Enter your age: "))
# Print a greeting using the name and age variables
print("Hello " + name + ", of age " + str(age))

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# Ask the user for the length of a rectangle and store it as an integer
length = int(input("Enter the length of the rectangle: "))
# Ask the user for the width of a rectangle and store it as an integer
width = int(input("Enter the width of the rectangle: "))
# Calculate the area of the rectangle
area = length * width
# Print the result
print("The area of the rectangle is: ", area)

#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# Ask the user for a temperature in Celsius and store it as a float
temperature_celsius = float(input("Enter the temperature in Celsius: "))
# Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
temperature_fahrenheit = (temperature_celsius * 9 / 5) + 32
# Print the result rounded to two decimal places
print("The temperature in Fahrenheit is: ", round(temperature_fahrenheit, 2))
