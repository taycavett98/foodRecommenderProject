import random
class Meals():
    def __init__(self,name,veggies1,veggies2,protein,carb,fat,sauce):
        self.name = name
        self.veggies1 = veggies1
        self.veggies2 = veggies2
        self.protein = protein
        self.carb = carb
        self.fat = fat
        self.sauce = sauce

    def printMeal(meal):
        print("meal: " + meal.name)
        print("ingredients: ")
        print( "\t" + meal.veggies1 , meal.veggies2, meal.protein , meal.carb , meal.fat , meal.sauce , sep = ' + ')
        print("Enjoy!")
        print("*************************************")

    veggies1 = ["power greens", "romaine"]
    veggies2 = [ "cauliflower", "brocolli", "b sprouts", "root blend", "mushrooms & onions", "asparagus"]
    protein = ["tuna", "sardines", "salmon", "bison", "beef", "chicken", "turkey", "eggs"]
    carb = ["pasta", "wild rice", "white rice", "fingerlings", "potato medley", "russet", "sweet potato", "purple potato", "japenese sweet potato", "bagel", "quinoa", "tortilla", "taco"]
    fat = ["pesto", "sunflower butter", "almond butter", "mixed nut butter", "avocado"] 
    sauce = ["none", "bbq", "avocado dressing", "oil & vinegar", "tzaziki", "salsa"]

# instances of class Meals
bowl1 = Meals("ever green wild rice bowl", Meals.veggies1[0] , Meals.veggies2[4] ,Meals.protein[1], Meals.carb[1], Meals.fat[0], Meals.sauce[0])
bowl2 = Meals("tex mex bowl", Meals.veggies1[1] , Meals.veggies2[4], Meals.protein[5], Meals.carb[10], Meals.fat[4], Meals.sauce[5])
bowl3 = Meals("mediterranean bowl", Meals.veggies1[0] , Meals.veggies2[0] ,Meals.protein[3], Meals.carb[10], Meals.fat[0], Meals.sauce[4])
bowl4 = Meals("bfast power bowl", Meals.veggies1[0], Meals.veggies2[5] , Meals.protein[7], Meals.carb[6], Meals.fat[4], Meals.sauce[0])

plate1 = Meals("hearty plate", Meals.veggies1[0], Meals.veggies2[3] , Meals.protein[3], Meals.carb[7], Meals.fat[3], Meals.sauce[1])
plate2 = Meals("power plate", Meals.veggies1[0], Meals.veggies2[2] , Meals.protein[4], Meals.carb[8], Meals.fat[2], Meals.sauce[0])
plate3 = Meals("level up plate", Meals.veggies1[0] , Meals.veggies2[4] ,Meals.protein[6], Meals.carb[9], Meals.fat[0], Meals.sauce[0])

# list of instances of class Meals
mealOptions = [bowl1, bowl2, bowl3, bowl4, plate1, plate2, plate3]

# declare empty list
inventory = []

def main():
    # ask user for any igredients
    # if none, continue to ask about what bowl they would want
    # if they have ingredients, allow them to store until they are done
    ingredientsOnHand = False
    print("Do you have any ingredients on hand ?")
    print("Enter 0 - No, 1 - Yes")
    userPantry = int(input())
    print()
    if (userPantry == 0):
        emptyPantry()
    else:
        fillPantry()
    for i in range(0, len(inventory)):
        print (inventory[i])
    print("would you like to show meal options exclusive to what you have on hand ?")
    print("Enter 0 - No, 1- Yes")
    combine = int(input())
    if(combine == 0):
        pass
    else:
        pass
    print("Goodbye")

# TODO:add type validation check
def showMenu():
    # display menu and get user input
    print("***MENU***")
    print(" Please select one of the following: ")
    print(" 0 - Random", " 1 - Pacific NW", " 2 - Mex", " 3 - Mediterraneam", " 4 - Quit", sep='\n')
    choice = int(input())
    return choice

def emptyPantry():
    choice = showMenu()
    while(choice != 4):
        if choice == 0:
            selection = random.choice(mealOptions)
        if choice == 1:
            selection = mealOptions[0]
        if choice == 2:
            selection = mealOptions[1]
        if choice == 3:
            selection = mealOptions[2]
        print()
        selection.printMeal()
        choice = showMenu()

# TODO: grab ingridients from user and store them in file using pickle
# idea: instead of individually having the different lists for the vegetables
# i could have 1 list and just keep up with what indexes we fill for each
# section of veg/carb/pro/fats/saucy. then if user wishes to combine
# this list with other ingredient options then sould be easier to combine 
# would have to combine from certain indexes like [vegIndex:carbIndex-1], then
# append to the main list

"""
    # get user input for ingredients on hand
    # create empty list
    inventory = []
    veg = []
    carb = []
    pro = []
    fats = []
    saucy = []
    # get user inventory
    n = int(input("how many ingredients do you have ? "))
    print("Ok, you have " + n + " ingredients to enter.")
    for i in range(0,n):
    print("veggies first!")
    print("how many veggies do you have on hand ? ")
    vegCount = int(input())
    print("enter your veggies ! ")
    for v in range(0,vegCount):
        veggies = input()
        veg.append(veggies)
    print("how many sources of carbs do you have on hand ?")
    carbCount = int(input())
    print ("enter your carb sources !")
    for c in range(0,carbCount):
        carbs = input()
        carb.append(carbs)
    print("how many proteins do you have on hand ? ")
    proCount = int (input())
    print("enter your protein !")
    for p in range(0,proCount):
        proteins = input()
        pro.append(proteins)
    print("how many fats do you have on hand ?")
    print("enter your fats !")
    fatCount = int(input())
    for f in range(0,fatCount):
        fat = input()
        fats.append(fat)
    
    item = input()
    inventory.append(item)
    print(inventory)
"""
def fillPantry():
    print("veggies first!")
    print("how many veggies do you have on hand ? ")
    vegCount = int(input())
    print("enter your veggies ! ")
    for v in range(0,vegCount):
        veggies = input()
        inventory.append(veggies)
    print("how many sources of carbs do you have on hand ?")
    carbCount = int(input())
    print ("enter your carb sources !")
    for c in range(vegCount, vegCount+carbCount):
        carbs = input()
        inventory.append(carbs)
    print("how many proteins do you have on hand ? ")
    proCount = int (input())
    print("enter your protein !")
    for p in range(carbCount,carbCount+proCount):
        proteins = input()
        inventory.append(proteins)
    print("how many fats do you have on hand ?")
    print("enter your fats !")
    fatCount = int(input())
    for f in range(proCount,proCount+fatCount):
        fat = input()
        inventory.append(fat)

main()