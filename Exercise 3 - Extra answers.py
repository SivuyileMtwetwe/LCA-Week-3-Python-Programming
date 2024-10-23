# #------------------------------------------------------------------------------------
# # Task 1: Function for Basic Real-Life Calculation

# # TODO: Define a function called 'calculate_discount' that takes an item's price and discount percentage as parameters, 
# #       and returns the discounted price.
# #       Example: If the price is 100 and the discount is 20%, it should return 80.
# def calculate_discount(price, discount):
    

#     return price - price*(discount/100)

# # TODO: Call the 'calculate_discount' function with a price of 250 and a discount of 15%, and print the result.
# print(calculate_discount(250,15))

#------------------------------------------------------------------------------------
# Task 2: Function with Multiple Parameters and Conditional Logic

# TODO: Define a function called 'shipping_cost' that takes the weight of a package and the destination 
#       (either "domestic" or "international") as parameters, and returns the shipping cost based on the following:
#       - For domestic shipping: $5 per kg.
#       - For international shipping: $15 per kg.

# weight = float(input("Enter weight of the package: "))
# destination = input("Enter destination, domestic or international? ")
def shipping_cost(weight,destination):
    

    if destination == "domestic":
       return weight*5
    elif destination == "international":
       return weight *15
    else:
        print("Error: Please check your selection.")

# TODO: Call the 'shipping_cost' function with a weight of 3kg and an "international" destination, and print the result.
print(shipping_cost(3,"international"))

#------------------------------------------------------------------------------------
# Task 3: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.
def check_attendance(students,absentees):
    absente_students = []
    present_students = []

    for student in students:
        if student in absentees:
            absente_students.append(student)
        else:
            present_students.append(student) 

    return absente_students,present_students
# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.
students = ["Alice", "Bob", "Charlie", "David"]
absentees = ["Bob", "David"]
present, absent = check_attendance(students, absentees)

print("Present students:", present)
print("Absent students:", absent)
#------------------------------------------------------------------------------------
# Task 4: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.
def calculate_average_grade(students):
    total = sum(students.values())
    count = len(students)
    average = total / count 
    return average

students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}

# Calculate and print the average grade
average_grade = calculate_average_grade(students)
print("The average grade of the class is:", average_grade)
    
# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.


#------------------------------------------------------------------------------------
# Task 5: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.

def operation_selector(operation):
    # Define the inner functions for adding and multiplying
    def add(x, y):
        return x + y
    
    def multiply(x, y):
        return x * y
    
    if operation == "add":
        return add
    elif operation == "multiply":
        return multiply
    else:
        return None  # Handle invalid operation

# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.
add_function = operation_selector("add")
result_add = add_function(4, 6)
print(result_add)  # Output: 10

# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.
multiply_function = operation_selector("multiply")
result_multiply = multiply_function(3, 7)
print(result_multiply) 
#------------------------------------------------------------------------------------
# Task 6: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.

distance = 150  
fuel_efficiency = 15  
fuel_price = 1.5  
def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
    
    
    fuel_needed = distance / fuel_efficiency
    
    total_cost = fuel_needed * fuel_price
    
    return total_cost


cost = calculate_trip_cost(distance, fuel_efficiency, fuel_price)
print(f"The total cost of the trip is: ${round(cost,2)}")
