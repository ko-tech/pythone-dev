def count_to_three():
    print("1")

def camp_input():
    count_to_three()

    adjective = input("Enter adjective here:")
    animal = input("Enter animal here:")
    second_animal = input("Enter second animal here:")
    second_adjective = input("Enter second adjective here:")
    noun = input("Enter noun here:")

    print("Camping is " + adjective + ", you might see a " + animal + " and a " + second_animal + ".")


    print("The food which is cooked over the " + noun + " is very " + second_adjective + ".")

if __name__ == "__main__":
    camp_input()

# TODO: 
# Create a function that you can call within the test.py
# Learn about the file writing and reading 
# Store the command line inputs to a txt or .csv file with the columns holding the variables that you are taking in