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

# 6-5: Polling -
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