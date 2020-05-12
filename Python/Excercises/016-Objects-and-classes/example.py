# ------------ 1 -----------#
# Create a class called fruit, with 2 variables, naam and weight


class Fruit:

    isEdible = True

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


# ------------ 2 ------------#
# Create 3 Fruit() objects
apple = Fruit("apple", 100)
papaya = Fruit("papaya", 500)
banana = Fruit("banana", 150)

# ------------ 3 ------------#
# Create a function that prints a sentence containing the
# variables from the Fruit() object


def fruitDescription(fruit):
    if fruit.isEdible:
        print(f"An {fruit.name} weights {fruit.weight} gram")


# ------------ 4 ------------#
# Change the weigth of ne one the Fruit() objects created
papaya.weight = 700

fruitDescription(apple)
fruitDescription(papaya)
fruitDescription(banana)
