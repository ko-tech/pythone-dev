#8-10: Great Magicians - 8-11: Unchange Magicians
def show_magicians(magicians_list):
    for magician in magicians_list:
        print("\n" + magician.title())

def make_great(magicians_list):
    return ["the great " + magician for magician in magicians_list]


magicians_list = ["bombozo", "david blaine", "criss angel"]
magicians_list2 = make_great(magicians_list)
show_magicians(magicians_list)

print(magicians_list2)
print(magicians_list)