class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print("The " + self.name.title() + " is a very restaurant with five stars with the type " + self.type)

    def open_restaurant(self):
        print("This restaurant is Open")

restaurante = Restaurant("Ramones", "Mar")
restaurante.describe_restaurant()
restaurante.open_restaurant()