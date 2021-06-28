class Dog:
    """Prosta klasa opisujaca psa"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name}")
        print(f"It serves {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant is now open!")

class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.greet_user()
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
    def greet_user(self):
        print(f"Witaj {self.first_name}")


pies=Dog("Dino",14)
print(f"Moj pies nazywa sie {pies.name}.\nOn ma {pies.age} lat.")
pies.sit()
pies.roll_over()

res1=Restaurant("Restauracja 1","ryby")
res2=Restaurant("Restauracja 2","psy")
res3=Restaurant("Restauracja 3","ptaki")

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()


u1=User("Daniel","Florek","daniel@wp.pl",22)
u1.describe_user()