# autos.py

class Auto():
    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

    def wash(self):
        print("WASHING THE CAR")

    def drive(self):
        print("WE ARE DRIVING", self.model)

class Truck(Auto):
    def __init__(self, make, model, year, color, num_wheels, bed_size):
        super().__init__(make, model, year, color, num_wheels)
        self.bed_size = bed_size
    
    def drive(self):
        print("WE ARE DRIVING", self.model, "WITH BED SIZE:", self.bed_size)

if __name__ == "__main__":
    car = Auto("Toyota", "Prius", 2020, "Blue", 4)
    print(car.make, car.model)
    car.drive()
    car.wash()
    
    car2 = Auto("Tesla", "Model S", 2020, "Blue", 4)
    car2.drive()
    car2.wash()
    
    truck = Truck("Ford", "F150", 2020, "Blue", 4, bed_size="5x5")
    truck.drive()
    truck.wash()
    
    truck2 = Truck("Tesla", "Cybertuck", 2020, "Blue", 4, bed_size="6x4")
    truck2.drive()
    truck2.wash()