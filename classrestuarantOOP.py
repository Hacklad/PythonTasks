### Task:

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}, we have {self.cuisine_type} cuisine here")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
    
restaurant = Restaurant('Aroma','Yoruba')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
