#8-16: Imports
def show_magicians(magicians_list):
    for magician in magicians_list:
        print("\n" + magician.title())

def make_great(magicians_list):
    return ["the great " + magician for magician in magicians_list]