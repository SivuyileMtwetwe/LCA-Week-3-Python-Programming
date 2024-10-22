#------------------------------------------------------------------------------------
# Task 1: Arithmetic and Assignment Operators (Advanced)

# TODO: Initialize a variable z with any value.
z =0
# TODO: Subtract 5 from z using the -= operator.
z -= 5
# TODO: Add the value of x to z using the += operator (Assume x is already defined).
x =0
z += x
# TODO: Divide z by 3 using the /= operator and store the result back in z.
z/=3

result = z
# TODO: Print the final value of z.
print(result)
#------------------------------------------------------------------------------------
# Task 2: Nested Comparison and Logical Operators

# TODO: Initialize three variables p, q, and r with different values.
p = 1
q = 2
r = 3

# TODO: Create a condition that checks if p is greater than q OR r is greater than q.
condition1 = p>q or r>q
# TODO: Also, check if p is less than or equal to r AND q is an even number.
condition2 = p<=r and q%2 == 0
# TODO: Combine these conditions using logical operators to create a 'complex_condition'.
complex_condition = condition1 or condition2
# TODO: Print the value of 'complex_condition'.
print(complex_condition)
#------------------------------------------------------------------------------------
# Task 3: Complex Conditional Statements

# TODO: Ask the user to input their age and store it in a variable 'age'.
age = int(input("Enter your age: "))
# TODO: If the age is 18 or above, print "Eligible to vote."
if age>= 18 :
    result = "Eligible to vote"
# TODO: If the age is between 13 and 17 (inclusive), print "Teenager."
elif age>=13 and age<=17:
    result = "Teenager"
# TODO: If the age is below 13, check if it is an even or odd number.
elif age<13 and age%2 == 0 :
    result = "Age is even"
else:
    result= "Age is odd"
# TODO: Print whether they are "even-aged" or "odd-aged" based on the result.
print(result)
#------------------------------------------------------------------------------------
# Task 4: Comparing Three Numbers

# TODO: Ask the user to input three numbers: a, b, and c.
# TODO: Compare the three numbers and print which one is the largest.
# TODO: If all three numbers are equal, print "All numbers are equal."
# TODO: If two numbers are equal and larger than the third, print the appropriate message.
a = float(input("Enter number: "))
b = float(input("Enter number: "))
c = float(input("Enter number: "))
if a == b == c:
    print("All numbers are equal")
elif a >= b and a >= c:
    if b == a:
        print("Numbers a and b are equal and largest:", a)
    elif c == a:
        print("Numbers a and c are equal and largest:", a)
    else:
        print("a is the largest number:", a)
elif b >= a and b >= c:
    if c == b:
        print("Numbers b and c are equal and largest:", b)
    else:
        print("b is the largest number:", b)
else:
    print("c is the largest number:", c)


#------------------------------------------------------------------------------------
# Task 5: Advanced Arithmetic and Logical Operations

# TODO: Ask the user to input two numbers: x and y.
x = float(input("Enter number: "))
y = float(input("Enter number: "))

# TODO: If both x and y are positive, print their sum
if x>=0 and y>=0:
   print(x+y) 
# TODO: If both x and y are negative, print their product.
elif x<0 and y<0:
    print(x*y)

# TODO: If one of them is positive and the other is negative, print their absolute difference.
elif (x<0 and y>0 ) or (y<0 and x>0):
      print(f"The absolute difference between {x} and {y} is {abs(x - y)}.")

# TODO: If both are zero, print "Both are zero."
elif x == 0 and y == 0:
    print("Both are zero.")
else:
    print("Done ")