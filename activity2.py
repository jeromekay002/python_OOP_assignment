# Create a program that includes animals or vehicles with the same action
# (like move()). However, make each class define move() differently
# (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

# polymorphisim is where diffrent classes have same method name 
# but each class behaves diffrently

class Car:
    def move(self):
        print("I am Driving")
class Plane:
    def move(self):
        print("I am Flying")

class Bike:
    def move(self):
        print("I am Cycling")

# lets test the polymorphisim
def start_moving(vehicle):
    vehicle.move()

# create instances of each class
my_car = Car()
my_plane = Plane()
my_bike = Bike()

start_moving(my_car)  
start_moving(my_plane)
start_moving(my_bike)