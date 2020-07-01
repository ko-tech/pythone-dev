#5-8: Hello admin: 
def hello_admin():
    usernames = ["admin", "faroukh", "lilcode", "rinxeo", "gando"]

    for username in usernames:
        if username == "admin":
            print("Hello Admin, would you like to see a status report?")
        else: 
            print("Hello " + username.title() + ", thank you for logging on.")

#5-9: No users:
def no_users():
    usernames = ["admin", "faroukh", "lilcode", "rinxeo", "gando"]

    if usernames:
        for username in usernames:
            print("Hello " + username.title() + ", welcome back!")
    else:
        print("We need to find more users!")

    usernames = []

    if usernames:
        for username in usernames:
            print("Hello " + username.title() + ", welcome back!")
    else:
        print("We need to find more users!")

#5-10: Checking Usernames:
def checking_username ():    
    current_users = ["lildicky", "faroukh", "lilcode", "forgiving", "sneAky"]

    new_users = ["bjergsen", "SNEAKY", "lildicky", "dyrus", "squishy"]

    current_users = [user.lower() for user in current_users]
    for user in new_users:
        if user.lower() in current_users:
            print("Username taken")
        else:
            print(user + " is available!")

#5-11: Ordinal Numbers:
def ordinal_numbers():
    numbers = [str(x) for x in range(1,10,1)]
    print(numbers)
    for number in numbers:
        if number == str(1):
            print(number + "st")
        elif number == str(2):
            print(number + "nd")
        elif number == str(3):
            print(number + "rd")
        else:
            print(number + "th")
print("Test")