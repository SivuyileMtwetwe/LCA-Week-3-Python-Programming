# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["apple", "orange", "banana", "grape", "lemon","mango","strawberry", "naartjies"]
# TODO: Add a fruit to the end of the list
fruits.append("peach")

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"pear")
# TODO: Remove a fruit from the list
fruits.remove("grape")
# TODO: Print the modified list
print(fruits)
 

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1,2,3,4,5]
# TODO: Create a new list with each number squared
new_list = []

for num in numbers:
    new_list.append(num**2)

print(new_list)
# TODO: Find the sum and average of the original numbers
sum_ = sum(numbers)
average = sum(numbers)/len(numbers)
# TODO: Print the results
print(sum_)

print(average) 

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_and_capitals = {
    "Afghanistan": "Kabul",
    "Albania": "Tirana",
    "Algeria": "Algiers",
    "Andorra": "Andorra la Vella",
    "Angola": "Luanda",
    "Argentina": "Buenos Aires",
    "Armenia": "Yerevan",
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Azerbaijan": "Baku",
    "Bahamas": "Nassau",
    "Bahrain": "Manama",
    "Bangladesh": "Dhaka",
    "Barbados": "Bridgetown",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Belize": "Belmopan",
    "Benin": "Porto-Novo",
    "Bhutan": "Thimphu"
}
# TODO: Add a new country-capital pair
countries_and_capitals["South Africa"] = "Pretoria"
# TODO: Update the capital of an existing country
countries_and_capitals["Afghanistan"] = "Tokyo"
# TODO: Remove a country-capital pair
countries_and_capitals.pop("Belgium")
# TODO: Print the modified dictionary
print(countries_and_capitals)
#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruits_and_color = {
    "Banana": "Yellow",
    "Blueberry": "Blue",
    "Lemon": "Yellow",
    "Lime": "Green",
    "Orange": "Orange",
    "Raspberry": "Red",
    "Strawberry": "Red",
    "Cherry": "Red",
    "Grapefruit": "Red",
    "Blackberry": "Black",
    "Cranberry": "Red",
    "Mango": "Orange",
    "Cantaloupe": "Orange",
    "Papaya": "Orange",
    "Pineapple": "Yellow",
    "Watermelon": "Red",
    "Apple": "Red/Green",
    "Grapes": "Green/Purple",
    "Peach": "Orange/Yellow",
    "Pear": "Green/Yellow",
    "Plum": "Purple",
    "Pomegranate": "Red",
    "Kiwi": "Green",
    "Dragonfruit": "Pink/White",
    "Passionfruit": "Purple",
    "Apricot": "Orange",
    "Mulberry": "Purple/Red",
    "Guava": "Green/Pink",
    "Jackfruit": "Yellow/Green",
    "Lychee": "Red",
    "Tangerine": "Orange",
    "Nectarine": "Orange",
    "Persimmon": "Orange",
    "Fig": "Purple/Green",
    "Quince": "Yellow",
    "Starfruit": "Yellow",
    "Avocado": "Green",
    "Coconut": "Brown",
    "Durian": "Green",
    "Honeydew": "Green",
    "Rambutan": "Red",
    "Boysenberry": "Purple",
    "Elderberry": "Black",
    "Gooseberry": "Green/Yellow",
    "Currant": "Red/Black",
    "Jujube": "Red/Brown",
}


# TODO: Print all the fruits (keys)
for fruit in fruits_and_color.keys():
    print(f"{fruit}")
# TODO: Print all the colors (values)
for color in fruits_and_color.values():
    print(f"{color}")
# TODO: Print each fruit and its color
for fruit,color in fruits_and_color.items():
    print(f"{fruit}: {color}")
# TODO: Check if a fruit is in the dictionary and print its color
fruit = str(input("Enter a fruit:").capitalize())
if fruit in fruits_and_color:
    print(f"{fruit} is in the dictionary and its color is {fruits_and_color[fruit]}")
else:
    print(f"{fruit} is not in the dictionary")
 
