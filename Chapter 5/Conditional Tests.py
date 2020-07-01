# 5-1: Write a series of conditional tests.
def conditional_test():
    car = "challenger"
    print("Is car == 'challenger'? I predict True")
    print(car == "challenger")

    print("Is car == 'charger'? I predict False")
    print(car == "charger")


    food = "pasta"
    print("\nIs food == 'pasta'? I predict True")
    print(food == "pasta")

    print("Is food == 'spaghetti'? I predict False")
    print(food == 'spaghetti')


    pizza = "veggie"
    print("\nIs pizza == 'veggie'? I predict True")
    print(pizza == 'veggie')

    print("Is pizza == 'meatlovers'? I predict False")
    print(pizza == 'meatlovers')

    hair = "black"
    print("\nIs hair == 'black'? I predict True")
    print(hair == 'black')

    print("Is hair == 'brown'? I predict False")
    print(hair == 'brown')

    dog = "golden retriever"
    print("\nIs dog == 'golden retriever'? I predict True")
    print(dog == 'golden retriever')

    print("Is dog == 'dalmation'? I predict False")
    print(dog == 'dalmation')

# 5-2: More Conditional tests

fav_car = "challenger"

if fav_car == "challenger":
    print("What's your favorite? Demon or Hellcat?")
if fav_car != "charger":
    print("\nWhy don't you like Challengers?")


usernames = ["squall", "trash", "user", "artist", "tanban", "axel"]
new_username = "ARTist"
new_username2 = "Faroukh"

if new_username.lower() in usernames:
    print("\nUsername not available")

if new_username2.lower() not in usernames:
    print("\nUsername available!")

# Rated R Movies must be accompanied by adult
allowed_age = 21
age_1 = 16
age_2 = 25
if age_1 >= allowed_age or age_2 >= allowed_age:
    print("You're allowed to watch the movie")
else:
    print("You're not allowed to watch the movie")

allowed_age = 21
age_1 = 16
age_2 = 25
if age_1 >= allowed_age and age_2 >= allowed_age:
    print("You're allowed to watch the movie")
else:
    print("You're not allowed to watch the movie")


