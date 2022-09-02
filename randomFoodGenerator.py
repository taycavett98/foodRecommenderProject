import random

foodRecipes = ["waffles", "rice and beans", "tacos", "pizza", "gyro"]
protein = ["venison", "salmon", "bison", "chicken", "turkey", "tempeh", "beef", "eggs", "beans", "tuna"]
veggies = ["broccoli", "cauliflower", "asparagus", "green beans", "mushrooms", "onion"]
carbs = ["potatoes", "white rice" , "wild rice", "pasta"]
fats = ["almond butter", "sunflower butter", "mixed nut butter", "avocado", "olive oil"]
sauce = ["bbq", "queso", "guac", "ketchup", "mustard", "pesto", "tzaziki"]

""""
# get user input for ingredients on hand
# create empty list
inventory = []
# get user inventory
n = int(input("how many ingredients do you have?"))
for i in range(0,n):
    item = input()
    inventory.append(item)
print(inventory)
"""
print("#############")

# search for ingredients that is in inventory
text = input("Randomly generate your bowl. Press enter")
if text == "":
    # randomly generate bowl using random module
    print("bowl: " , random.choice(protein), " + ", random.choice(veggies)," + ", random.choice(carbs), " + ",random.choice(fats), " + ",random.choice(sauce))
else:
    print("fail")


