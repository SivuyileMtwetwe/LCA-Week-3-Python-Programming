#Statement here



num_of_people = int(input("How many people are you ordering for? "))
num_slices = int(input("How many slices would each person want? "))

def pizza_amount(num_of_people, num_slices):
    total_slices = num_of_people * num_slices
    return total_slices

total_slices = pizza_amount(num_of_people, num_slices)

print(f"You will need {total_slices} slices of pizza.")
 
