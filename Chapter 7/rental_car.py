# 7-1: Rental Car -
def rental_car():
    car = input("What car are you looking for?: ")
    print("Let me see if if I can find a " + car.title() + " in the yard.")

# 7-2: Restaurant Setting - 
def restaurant_setting():    
    group_size = input("How many people will be dining today: ")

    if int(group_size) >= 8:
        print("The wait is approximately " + group_size + " minutes.")
    else:
        print("Come this way to be seated.")

# 7-3: Multiples of ten -
def multiples_of_ten():
    number = input("What's your favorite number: ")

    if 10 % int(number):
        print(number + " is a multiple of ten")
    else:
        print(number + " is not a multiple of ten")

# 7-4: Pizza Toppings - 
def pizza_toppings():
    prompt = "\nTell me what toppings you want on your pizza,"
    prompt += "\nsay 'stop' when you're done: "
    toppings = []
    message = ""
    while message != 'stop':
        message = input(prompt)
        if message != 'stop':
            print("Adding " + message + " to the pizza!")
        if message != 'stop':
            toppings.append(message)

    print("\nSo you want a pizza with:")
    print(toppings)
    input("\nIs that all: ")

# 7-5: Movie Tickets - 
def movie_tickets():
    while True:
        prompt = input("\nAge: ")

        if int(prompt) < 3:
            price = "no charge"
        elif int(prompt) >= 3 and int(prompt) <= 12:
            price = "$10"
        elif int(prompt) > 12:
            price = "$15"
        print("\nYour cost is " + price)
    
# 7-6: Three Exits - 
def three_exits():

    prompt = "\nTell me what toppings you want on your pizza,"
    prompt += "\nsay 'stop' when you're done: "
    message = "" 
    while message != 'stop':
        message = input(prompt)
        if message != 'stop':
            print("Adding " + message + " to the pizza!")
        if message == 'stop':
            break

    prompt = "\nTell me what toppings you want on your pizza,"
    prompt += "\nsay 'stop' when you're done: "
    toppings = []
    message = ""
    active = True
    while active or message != 'stop':
        message = input(prompt)
        if message != 'stop':
            print("Adding " + message + " to the pizza!")
        if message != 'stop':
            toppings.append(message)
        if len(toppings) >= 5:
            active = False

    print("\nSo you want a pizza with:")
    print(toppings)
    input("\nIs that all: ")

#7-7: Infinity - 
def infinity():
    prompt = input("\nAge: ")
    while True:
        

        if int(prompt) < 3:
            price = "no charge"
        elif int(prompt) >= 3 and int(prompt) <= 12:
            price = "$10"
        elif int(prompt) > 12:
            price = "$15"
        print("\nYour cost is " + price)
# 7-8: Deli - 
def deli():
    sandwich_orders = ["ham & cheese", "veggie", "pb&j", "meatlovers"]
    finished_sandwiches = []

    while sandwich_orders: 
        finished_sandwich = sandwich_orders.pop()
        print("\nYour " + finished_sandwich.title() + " is finished!")
        finished_sandwiches.append(finished_sandwich)

    print("\nThe following sandwiches were made:")
    print(finished_sandwiches)

# 7-9: No Pastrami -
def no_pastrami():
    sandwich_orders = ["ham & cheese", "pastrami", "veggie", "pastrami", "pb&j", "pastrami", "meatlovers"]
    finished_sandwiches = []
    print("We've run out of pastrami")
    while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")
    while sandwich_orders: 
        finished_sandwich = sandwich_orders.pop()
        print("\nYour " + finished_sandwich.title() + " is finished!")
        finished_sandwiches.append(finished_sandwich)

# 7-10: Dream Vacation - 
def dream_vacation():   
    dream_vacation = {}
    polling_active = True

    while polling_active:
        name = input("\nWhat is your name? ")
        location = input("Where is your dream vacation? ")
        dream_vacation[name] = location
        repeat = input("would you like to let another person respond? ")
        if repeat == 'no':
            polling_active = False

    print("\nSurvey Results:")
    for name, location in dream_vacation.items():
        print("\n" + name.title() + " would like to go to " + location.title())
