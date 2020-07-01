# 4-10: Slices: 
def pizzas():
    office_accesories = ["calculator", "glasses", "stamp", "phone", "stapler", "printer"]

    print("The first 3 items in the list are:")
    print(office_accesories[0:3])
    print("\nThree items from the middle of the list are:")
    print(office_accesories[1:5])
    print("\nThe last three items in the list are:")
    print(office_accesories[3:])

# 4-11: My Pizzas, Your Pizzas:
def my_pizzas_your_pizzas():
    my_pizzas = ["pepperoni", "cheese", "hawaiian", "meatlovers"]
    friends_pizzas = my_pizzas[:]

    my_pizzas.append("veggie")
    friends_pizzas.append("tofu")

    print("My favorite pizzas are:")
    for pizza in my_pizzas:
        print(pizza)

    print("\nMy friend's favorite pizzas are:")
    for pizza in friends_pizzas:
        print(pizza)

# 4-12: Loops:
def loops():
    my_foods = ['pizza', 'falafel', 'carrot cake'] 
    print("These are definitely not my favorite foods:")
    for food in my_foods:
        print(food)

# 4-13: Buffet:
def buffet_foods():
    buffet_foods = ("rice", "spaghetti", "soup", "salad", "chicken")

    print("This is the original menu:")
    for food in buffet_foods:
        print(food)

    buffet_foods = ("rice", "lentils", "soup", "beans", "chicken")
    print("\nThis is the new menu:")
    for food in buffet_foods:
        print(food)