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
