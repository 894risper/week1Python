# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Child class Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model)  # Inherit brand & model
        self.year = year
        self.color = color
    
    def start(self):
        print(f"{self.brand} {self.model} is starting... ")

    def display_info(self):   # Polymorphism (method overriding)
        print(f"{self.year} {self.color} {self.brand} {self.model}")

# Create objects
car1 = Car("Toyota", "Corolla", 2022, "Red")
car2 = Car("Honda", "Civic", 2023, "Black")

car1.start()
car1.display_info()

car2.start()
car2.display_info()
