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
        print("ingredients: " , meal.veggies1 , meal.veggies2, meal.protein , meal.carb , meal.fat , meal.sauce , sep = ' , ')

    veggies1 = ["power greens", "romaine"]
    veggies2 = [ "cauliflower", "brocolli", "b sprouts", "root blend", "mushrooms & onions", "asparagus"]
    protein = ["tuna", "sardines", "salmon", "bison", "beef", "chicken", "turkey", "eggs"] # 8
    carb = ["pasta", "wild rice", "white rice", "fingerlings", "potato medley", "russet", "sweet potato", "purple potato", "japenese sweet potato", "bagel", "quinoa", "tortilla", "taco"]
    fat = ["pesto", "sunflower butter", "almond butter", "mixed nut butter", "avocado"] # 5
    sauce = ["none", "bbq", "avocado dressing", "oil & vinegar", "tzaziki", "salsa"]

bowl1 = Meals("ever green wild rice bowl", Meals.veggies1[0] , Meals.veggies2[4] ,Meals.protein[1], Meals.carb[1], Meals.fat[0], Meals.sauce[0])
bowl2 = Meals("tex mex bowl", Meals.veggies1[1] , Meals.veggies2[4], Meals.protein[5], Meals.carb[10], Meals.fat[4], Meals.sauce[5])
bowl3 = Meals("mediterranean bowl", Meals.veggies1[0] , Meals.veggies2[0] ,Meals.protein[3], Meals.carb[10], Meals.fat[0], Meals.sauce[4])
bowl4 = Meals("bfast power bowl", Meals.veggies1[0], Meals.veggies2[5] , Meals.protein[7], Meals.carb[6], Meals.fat[4], Meals.sauce[0])

plate1 = Meals("hearty plate", Meals.veggies1[0], Meals.veggies2[3] , Meals.protein[3], Meals.carb[7], Meals.fat[3], Meals.sauce[1])
plate2 = Meals("power plate", Meals.veggies1[0], Meals.veggies2[2] , Meals.protein[4], Meals.carb[8], Meals.fat[2], Meals.sauce[0])
plate3 = Meals("level up plate", Meals.veggies1[0] , Meals.veggies2[4] ,Meals.protein[6], Meals.carb[9], Meals.fat[0], Meals.sauce[0])
#bowl1a.printMeal()

# use random to generate one of the premade selections
mealOptions = [bowl1, bowl2, bowl3, bowl4, plate1, plate2, plate3]


# display menu
print("MENU")
print("Please select one of the following: ")
choice = int(input(print("0 - Random", "1 - Pacific NW", "2 - Mex", "3 - Mediterraneam", "4 - Quit")))
while(choice != 4):
    
    if choice == 0:
        selection = random.choice(mealOptions)
    if choice == 1:
        selection = mealOptions[0]
    if choice == 2:
        selection = mealOptions[2]
    if choice == 3:
        selection = mealOptions[1]
selection.printMeal()
            
