class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
            print(self.name.title() + " is now sitting.")

    def roll_over(self):
            print(self.name.title() + " rolled over!")

my_dog = Dog("William", 8) #Instancia
your_dog = Dog("Pit", 6) #Instancia

print("My Dog's name is " + my_dog.name.title() + ".")
print("My Dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()

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


my_new_car = Car("Audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(32)
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

class ElectricCar(Car):
    def __init__(self, make, model, year, baterry_size):
        super().__init__(make, model, year)
        self.baterry_size = baterry_size
    def baterry(self):
        print("This car has a " + str(self.baterry_size) + "-kWh baterry")

    def fill_gas_tank(self):
        print("This car doens't need a gas tank!")

my_tesla = ElectricCar("tesla", "model s", 2016, 70)
print(my_tesla.get_descriptive_name())
my_tesla.baterry()