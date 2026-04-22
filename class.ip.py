print("=== Inheretance ===")

'''                                               N O T E S
Parent > Child
Parent class provides properties=>(states & method) only public or protected status  
'''


class Animal:
    description = "this class is parent for animals"

    def __init__(self, voice):
        self.status = "this animal is alive"
        self.voice = voice

    def makeVoice(self):
        print(f"This animal can make voice: {self.voice}")


class Dog(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f'{self.name} says: {self.sound} - {self.sound}')

    def protects(self):
        print(f'Yes, I can protect you')

    def makeVoice(self):
        print(f"The {self.name} says: {self.sound}")


class Cat(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def plays(self):
        print(f'the cat {self.name} loves to play with various games')

    def voiceEatting(self):
        print(f'{self.name} make {self.sound} while eating')


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)

dog.introduce()
cat.introduce()

print('=== with inheretance ===')

dog.makeVoice()
cat.makeVoice()

print('dog status:', dog.status)
print('cat status:', cat.status)

print('=== Polymorphism ===')

dog.makeVoice()
cat.makeVoice()

# Polymorphism => bir xil methodning xar xil shakillarni bolishi va inheretance qonuniyatiga ko'ra
# child classi o'zining tarkibida soralyotgan method ni topsa ushani ishlatadi agar yoq bolsa parentdan ushbu methodni  qabul qiladi.

a = isinstance(cat, Cat)
b = isinstance(dog, Animal)
c = isinstance(cat, object)
d = isinstance("MIT", object)
result = a and b and c and d
print('the result:', result)
