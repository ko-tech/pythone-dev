# 6-1: Person - 
def person():
    friend_01 = {"first_name" : "shawn", 
        "last_name" : "mcgann",
        "age" : 25,
        "city" : "hollywood"
        }

    print(friend_01["first_name"].title())
    print(friend_01["last_name"].title())
    print(friend_01["age"])
    print(friend_01["city"].title())

# 6-2: Favorite numbers -
def favorite_numbers():
    
    favorite_numbers = {"derek" : 52,
        "shawn" : 35,
        "eddy" : 25,
        "dennis" : 37,
        "gus" : 42,
        }

    for person in favorite_numbers:
        print(person.title() + "'s favorite number is " + str(favorite_numbers[person]))

# 6-3: Glossary - 
def glossary():
    coding_glossary = {"string" : "a sequence of characters",
        "integer" : "positive or negative whole numbers",
        "float" : "real numbers with decimal points",
        "boolean" : "binary variable having two possible values",
        "tuple" : "collection of objects that are immutable",
        }   
    print("String: " + coding_glossary["string"])
    print("\nFloat: " + coding_glossary["float"])
    print("\nInteger: " + coding_glossary["integer"])
    print("\nBoolean: " + coding_glossary["boolean"])
    print("\nTuple: " + coding_glossary["tuple"])

# 6-4: Glossary 2 -
def glossary2 (): 
    coding_glossary = {"string" : "a sequence of characters",
        "integer" : "positive or negative whole numbers",
        "float" : "real numbers with decimal points",
        "boolean" : "binary variable having two possible values",
        "tuple" : "collection of objects that are immutable",
        }  
    for word, definition in coding_glossary.items():
        print("\n" + word.title() + ": " + definition)

# 6-5: Rivers -
def rivers():
    major_rivers = {"nile" : "africa",
        "amazon" : "south america",
        "yangtze" : "china",
        }

    for river, country in major_rivers.items():
        print("\nThe " + river.title() + " river is located in " + country.title())

    for river in major_rivers.keys():
        print(river.title())

    for country in major_rivers.values():
        print(country.title())

# 6-6: Polling -
def polling():    
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

    people = ["jen", "edward", "kevin", "shawn", "eddy"]

    for person in people: 
        if person in favorite_languages.keys():
            print("\n" + person.title() + ", thank you for responding!")
        else:
            print("\n" + person.title() + ", please remember to take the poll.")

# 6-7: People - 
def people():
    friend_01 = {"first_name" : "shawn", 
        "last_name" : "mcgann",
        "age" : 25,
        "city" : "hollywood"
        }

    friend_02 = {"first_name" : "eddy", 
        "last_name" : "varela",
        "age" : 22,
        "city" : "hialeah"
        }

    friend_03 = {"first_name" : "kevin", 
        "last_name" : "osorio",
        "age" : 22,
        "city" : "hialeah"
        }

    friends = [friend_01, friend_02, friend_03]

    for friend in friends:
        print("\nFull Name: " + friend["first_name"].title() + " " + friend["last_name"].title())
        print("\tAge: " + str(friend["age"]))
        print("\tCity: " + friend["city"].title())

# 6-8: Pets -
def pets():
    luna = {"pet_name" : "luna",
        "owner_name" : "kevin",
        "animal" : "dog"}
    goliath = {"pet_name" : "goliath",
        "owner_name" : "yonny",
        "animal" : "dog"}
    kitty = {"pet_name" : "kitty",
        "owner_name" : "natalie",
        "animal" : "cat"}
    cookie = {"pet_name" : "cookie",
        "owner_name" : "lina",
        "animal" : "dog"}


    pets = [luna, goliath, kitty, cookie]

    for pet in pets:
        print("\nPet name: " + pet["pet_name"].title())
        print("Type of pet: " + pet["animal"].title())
        print("Owner: " + pet["owner_name"].title())

# 6-9: Favorite places - 
def favorite_places():   
    favorite_places = {"eddy" : ["new york", "seattle", "boston"],
        "shawn" : ["minessota", "south carolina", "jupiter"],
        "kevin" : ["tokyo", "amsterdam", "australia"],
        }

    for person, places in favorite_places.items():
        print("\n" + person.title() + "'s favorite places are:")
        for place in places:
            print(place.title())

# 6-10: Favorite Numbers 2 - 
def favorite_numbers2():
    favorite_numbers = {"derek" : [52, 96, 38],
        "shawn" : [35, 78, 38],
        "eddy" : [25, 21, 56],
        "dennis" : [37, 125, 63],
        "gus" : [42, 69, 28],
        }

    for person, numbers in favorite_numbers.items():
        print("\n" + person.title() + "'s favorite numbers are: ")
        for number in numbers:
            print(number)

# 6-11: Cities - 

cities = {
    "bangkok" : {
        "country" : "thailand",
        "population" : 22.78,
        "fact" : "hangover movie",
        },
    "paris" : {
        "country" : "france",
        "population" : 19.10,
        "fact" : "eiffel tower",
        },
    "london" : {
        "country" : "uk",
        "population" : 19.09,
        "fact" : "clock",
        },
    }

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    country = city_info["country"]
    population = city_info["population"]
    fact = city_info["fact"]

    print("Country: " + country.title())
    print("Population: " + str(population) + " Million")
    print("Fun fact: " + fact.title())

# 6-12: Expand on all operations above