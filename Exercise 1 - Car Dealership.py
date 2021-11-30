class Car:
    def __init__(self, make, model, year, odometer, colour, price):
        self.make = make
        self.year = year
        self.model = model
        self.odometer = odometer
        self.colour = colour
        self.price = price
    def car_information(self):
        print()
        print("The make of the car is",self.make)
        print("The model of the car is",self.model)
        print("The year the car was made was",str(self.year))
        print("The type of odometer the car has is",self.odometer)
        print("The color of the car is",self.colour)
        print("The price of the car is $"+str(self.price))

vehicle1 = Car("Lexus", "LC 500", "2001", "Mechanical", "Red", "1000")
vehicle2 = Car("Ford", "Water Bottle", "1991", "Digital", "Blue", "1500")
vehicle3 = Car("BMW", "Sauce", "1200", "Mechanical", "Yellow", "1040")
vehicle4 = Car("Chevrolet", "Guacamole", "1945", "Mechanical", "Green", "4200")
vehicle5 = Car("Mitsubishi", "Nuggets", "1835", "Mechanical", "Cyan", "6031")
vehicle6 = Car("Tesla", "Fruit", "5014", "Mechanical", "Magenta", "1456")

lot = [vehicle1,vehicle2,vehicle3,vehicle4,vehicle5,vehicle6]

for i in lot:
    i.car_information()