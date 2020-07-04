#8-1: Message - 
def display_message():
    """What I'm Learning"""
    print("This lesson I'll be learning about functions")

#8-2: Favorite Book - 
def favorite_book(title):
    """What my favorite book is"""
    print("My favorite book is the " + title.title())

#8-3: TShirt - 
def make_shirt(message, size):
    print("I have a " + size + " shirt that reads " + message)

#8-4: Large Shirts:
def make_shirt2(message="'I love Python'", size="large"):
    print("I have a " + size + " shirt that reads " + message)

#8-5: Cities - 
def describe_city(city, country="Colombia"):
    print("\n" + city.title() + " is in " + country.title())

#8-6: City Names - 
def city_country(city, country):
    location = city.title() + ", " + country.title()
    return location

    area = city_country("medellin", "colombia")
    print("\n" + area)

    area = city_country("miami", "united states")
    print("\n" + area)

    area = city_country("sao paulo", "brazil")
    print("\n" + area)

#8-7: Album -
def make_album(artist_name, album_title, tracks = ''):
    album = {"artist" : artist_name.title(),
        "album" : album_title.title()}
    if tracks:
        album["tracks"] = tracks
    return album

    favorite_album = make_album("kendrick lamar", "how to pimp a butterfly")
    print(favorite_album)

    favorite_album = make_album("pop smoke", "shoot for the stars aim for the moon")
    print(favorite_album)

    favorite_album = make_album("MGMT", "little dark age")
    print(favorite_album)

    favorite_album = make_album("russ", "there's really a wolf", 20)
    print(favorite_album)

#8-8: User albums - 
def make_album2(artist_name, album_title, tracks):
    album = {"artist" : artist_name.title(),
        "album" : album_title.title(),
        "tracks" : tracks}
    return album
while True:
    print("\nWhat's your favorite album?")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist == "q":
        break

    album = input("Album name: ")
    if album == "q":
        break

    tracks = input("Number of tracks: ")
    if tracks == "q":
        break

    user_album = make_album2(artist, album, int(tracks))
    print(user_album)