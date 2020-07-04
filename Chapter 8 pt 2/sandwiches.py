#8-12: Sandwiches -
def make_sanwich(*ingredients):
    print("Sandwich being made with: ")
    for ingredient in ingredients:
        print(" - " + ingredient.title())

make_sanwich("salami", "pepperoni", "ham", "cheese",)
make_sanwich("ham")
make_sanwich("ham", "cheese", "mayonaisee")