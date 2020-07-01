# 5-3: Alien Colors:
def alien_colors():
    alien_color = "red"

    if alien_color == "green":
        print("Earned 5 points!")

    if alien_color == "red":
        print("Earned 10 points!")

# 5-4: Alien Colors #2:
def alien_colors2():
    alien_color2 = "green"
    alien_color3 = "yellow"


    if alien_color2 == "green":
        print("Earned 5 points!")
    else:
        print("Earned 10 points!")

    if alien_color3 == "green":
        print("Earned 5 points!")
    else:
        print("Earned 10 points!")

# 5-5: Alien Colors #3:
def alien_colors3 ():

    alien_color = "green"

    if alien_color == "green":
        print("Earned 5 points!")
    elif alien_color == "yellow":
        print("Earned 10 points!")
    else:
        print("Earned 15 points!")

    alien_color = "yellow"

    if alien_color == "green":
        print("Earned 5 points!")
    elif alien_color == "yellow":
        print("Earned 10 points!")
    else:
        print("Earned 15 points!")

    alien_color = "red"

    if alien_color == "green":
        print("Earned 5 points!")
    elif alien_color == "yellow":
        print("Earned 10 points!")
    else:
        print("Earned 15 points!")

# 5-6: Stages of life:
def stages_of_life ():

    user_age = 33

    if user_age < 2:
        print("User is a child") 
    elif user_age >= 2 and user_age < 4:
        print("User is a toddler")
    elif user_age >= 4 and user_age < 13:
        print("User is a kid")
    elif user_age >= 13 and user_age < 20:
        print("User is a teenager")
    elif user_age >= 20 and user_age < 65:
        print("User is an adult")
    elif user_age >= 65:
        print("User is an elder")

# 5-7: Favorite Fruit:
favorite_fruits = ["banana", "mango", "strawberry"]

for fruit in favorite_fruits:
    if fruit == "banana":
        print("Bananas are good source of potassium")
    if fruit == "mango":
            print("I hate how mango always gets stuck in your teeth")
    if fruit == "strawberry":
        print("By itself I don't like it too much but it's great in smoothies")
    if fruit == "banana" or fruit == "strawberry":
        print("Strawberry & banana smoothies are the best combination")
    if fruit == "banana" or fruit == "mango":
        print("Though mango & banana are up there too")