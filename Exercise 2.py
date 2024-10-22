# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 0
x +=3 

# # TODO: Multiply y by 2 using the *= operator
y = 1

y*=2

# TODO: Divide x by y and store the result in a variable called 'result'

result = x/y

# TODO: Print the value of 'result'

print(f"The answer is {result}")
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = 4
b = 2
c = 3
condition1 = a>b

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)

condition2 = b%2 == 0


# TODO: Create a condition that checks if c is less than or equal to a

condition3 = c<=a


# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a

final_condition = (condition1) or (condition2 and condition3)

# TODO: Print the value of 'final_condition'
print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'

score = int(input("Enter your test score which should be between 0 and 100: "))

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F

if score>=90 and score<=100:
     grade = "A"
elif score>=80 and score<90:
     grade = "B"
elif score>=70 and score<80:
     grade = "C"
elif score>=60 and score<70:
     grade = "D"
else: 
     grade = "F"
# TODO: Print the grade for the given score
print(f"You get {grade} for your grade")
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'

operation = input("Enter operation (+, -, *, /): ")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
result = None

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2

# TODO: Handle the case of division by zero

elif operation == '/':
    if num2 != 0: 
        result = num1 / num2
    else:
        print("Error: Division by zero!")
        exit()
else:
    print("Invalid operation!")
    exit()

# TODO: Print the result of the operation

print(f"Result: {result}")

