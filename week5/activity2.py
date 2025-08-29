# Base class
class Vehicle:
    def move(self):
        print("This vehicle is moving")

# Subclass Car
class Car(Vehicle):
    def move(self):
        print("The car is driving ")

# Subclass Plane
class Plane(Vehicle):
    def move(self):
        print("The plane is flying ")

# Subclass Boat
class Boat(Vehicle):
    def move(self):
        print("The boat is sailing ")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
