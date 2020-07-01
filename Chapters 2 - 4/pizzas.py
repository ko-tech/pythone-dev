# 4.1: Pizzas
def pizzas():
    
    pizzas = ["pepperoni pizza", "meat-lovers pizza", "hawaiian pizza", "veggie pizza"]

    for pizza in pizzas:
        print(pizza.title() + " is delicious\n")
    print("\n\nThese are all my favorite pizzas")

# 4.2: Animals
def pets():
    animals = ["goldfish", "dogs", "cats", "snakes"]

    for animal in animals:
        print(animal.title() + " are easy to take care of")
        print(animal.title() + " are fun to have\n")
    print("These are all good pets to have")

# 4.3: Counting to Twenty
def twenty():
    for value in range(1,21):
        print(value)    

# 4.4 One Million:
def onemillion():
    numbers = list(range(1,1000001,))
    print(numbers)
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))

# 4.6: Odd Numbers
def odd_number():
    for odd_number in range(1,20,2):
        print(odd_number)

#4.7: Threes
def threes():
    threes = []
    for value in range(3,31):
        threes.append(value*3)
    print(threes)
    for integer in threes:
        print(integer)

#4.8: Cubes
def cubes():
    cubes = []
    for value in range(1,11):
        cubes.append(value**3)
    print(cubes)
    for integer in cubes:
        print(integer)

#4.9 Cubes Comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)