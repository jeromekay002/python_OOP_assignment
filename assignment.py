# Create a class representing anything you like
#  (a Smartphone, Book, or even a Superhero!).

# this is the parent class
class smartphone:
    # Add attributes and methods to bring the class to life!
    def __init__(self, brand, model, storage, batterylife, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.batterylife = batterylife
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Battery Life: {self.batterylife} hours")
        print(f"Color: {self.color}")
    
    # Add a method to simulate a phone call
    def make_call(self, contact):
        print(f"Calling {contact} using {self.brand}")
    
# child class
class smartphone_with_camera(smartphone):
    def __init__(self, brand, model, storage, batterylife, color):
        # super() is a biult in function used inside a child class 
        # to call a method from its parent class
        # i will reuse the parent's setup to set up the child class
        super().__init__(brand, model, storage, batterylife, color)

    # Add a method to take a photo
    def take_photo(self):
        print(f"Taking a photo with {self.brand} {self.model} camera!")


# lets create an example usage of the class
phone = smartphone_with_camera("Infinix", "HOT50Pro", 256, 33, "Sleek Black")
phone.display_info()
phone.make_call("Jerome")
phone.take_photo()
