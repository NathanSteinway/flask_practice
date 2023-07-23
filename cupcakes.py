from abc import ABC, abstractmethod
from pprint import pprint

import csv

# with open("sample.csv") as csvfile:
#     reader = csv.DictReader(csvfile)

#     for row in reader:
#         pprint(row)

class Cupcake(ABC):

    size = "regular"

    def __init__(self, name, price, cake, filling, icing):
        self.name = name
        self.price = price
        self.cake = cake
        self.filling = filling
        self.icing = icing
        self.topping = []

    def add_toppings(self, *args):
        for topping in args:
            self.topping.append(topping)

    def calculate_price(self, quantity):
        return quantity * self.price
    
class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, cake, icing, filling):
        self.name = name
        self.price = price
        self.cake = cake
        self.icing = icing
        self.filling = filling
        self.topping = []
        
first_cupcake = Cupcake('Choco-Dream', 2.99, 'chocolate', 'chocolate', 'chocolate')

first_cupcake.add_toppings('Oreo Crumbs', 'Rainbow', 'Vanilla')

second_Mini = Mini("Sorbet-Day", 3.99, "Orange Sorbet", "Pomogranate Sorbet", "Peach Sorbet")
print(second_Mini.name)
print(second_Mini.price)
print(second_Mini.size)

cupcake1 = Cupcake("Grandma's Fav", 4.99, "Cookies and Cream", "Chocolate", None)
cupcake2 = Mini("Little League", .99, "Chocolate", "Chocolate", "Vanilla")
cupcake3 = Mini("Huge", 9.99, "Hot Sauce", "Gunpowder", "Mean Words")
cupcake4 = Cupcake("Yordle Cupcake", 0.99, "Teemo", "Caitlyn", None)
cupcake5 = Mini("Mini Yordle Cupcake", 0.99, "Lulu", "Kai'Sa", "Chocolate")

cupcake_list = [cupcake1, cupcake2, cupcake3, cupcake4, cupcake5]

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["name", "price", "cake", "icing", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"name": cupcake.name, "price": cupcake.price, "cake": cupcake.cake, "icing": cupcake.icing, "filling": cupcake.filling}) 
            else:
                writer.writerow({"name": cupcake.name, "price": cupcake.price, "cake": cupcake.cake, "icing": cupcake.icing, "filling": cupcake.filling})

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader
    
def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["name", "price", "cake", "icing", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"name": cupcake.name, "price": cupcake.price, "cake": cupcake.cake, "icing": cupcake.icing, "filling": cupcake.filling})
        else:
            writer.writerow({"name": cupcake.name, "price": cupcake.price, "cake": cupcake.cake, "icing": cupcake.icing, "filling": cupcake.filling})

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["name", "price", "cake", "icing", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

write_new_csv("sample.csv", cupcake_list)
