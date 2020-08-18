class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def fill_gas_tank(self):
        print("This car need a gas tank!")

class ElectricCar(Car):
    def __init__(self, make, model, year, baterry_size):
        super().__init__(make, model, year)
        self.baterry_size = baterry_size
    def baterry(self):
        print("This car has a " + str(self.baterry_size) + "-kWh baterry")

    def fill_gas_tank(self):
        print("This car doens't need a gas tank!")