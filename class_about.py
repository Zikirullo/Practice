print("=== What's class ===")

# Blue print ya'ni shablon(template)
# structure => state, constructor, method lari bor


class Person():
    # state
    message = "class state property"
# constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age
# method

    def introduce(self):
        print(f"{self.name} says: How do you do")

    def says_age(self):
        print(f"{self.name} says I'm {self.age}!")

    @classmethod
    def explains(cls):
        print("static method property executed")


person1 = Person("Zikirullo", 21)
person2 = Person("Levi", 22)

# ordinary state property
print("person1.name", person1.name)
# ordinary method
person1.introduce()
person2.says_age()

print("=== Ordinary vs static properties")

# static propertylar class billan birga keladi
new_message = Person.message
print("new message:", new_message)

# static
Person.explains()

print("=== Special method ===")
# Python's most common special/magic methods:
# __inin__, __new__, __str__, __call__, __getitem__, __eq__, __len__, .....


class Car():
    description = "this class makes car"

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        print(f"the {self.brand} started engine")

    def stop_engine(self):
        print(f"the {self.brand} stopped engine")

    def __str__(self):
        return f"the car brand id {self.brand} and it was produced in {self.year}"

    def __call__(self):
        print("Object was called as a function!")


my_car = Car("Ferrari", 2026)
my_car.start_engine()
my_car.stop_engine()

your_car = Car("Toyota", 2012)
print(your_car)
print(my_car)
your_car()
my_car()
