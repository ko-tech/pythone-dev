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
prompt = input("\nAge: ")

if int(prompt) < 3:
    price = "no charge"
elif int(prompt) >= 3 and int(prompt) <= 12:
    price = "$10"
elif int(prompt) > 12:
    price = "$15"

