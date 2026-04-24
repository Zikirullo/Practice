print('=== tuples ===')

'''
lists vs tuples 
tuplse's values cannot be changes!
'''
# literal
num = [1, 3, 5, 7]

# construstor
letters = list('Hello world!')

fruits = ["apple", "banana", "kiwi", "lemon"]
print(f"{fruits}")

const = fruits[0]
print(const)
fruits[2] = "melon"
print(fruits)

# tuples cannot be mutted
animal = ("tiger", "monkey", "donkey", "dog")
tuple_obj = ("MIT43", 2026, True)

print(animal[0])

print(animal)

print("=== Unpackiing arguments ===")

groups = ["MIT", "Flexy", "Devex", "MG"]
(x, y, *z) = groups
print(f"z: {z}")


def calculate(*args):
    print("*args", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


calculate(1, 7, 4, 5)
print('--------------')
calculate(0, 2, 300)
print('--------------')
calculate(5, 7)

print("=== kwargs ===")


def introduce(**kwargs):
    print(f"type of **kwargs => {type(kwargs)}")
    print(f"Hi I'm {kwargs["name"]} and I'm {kwargs["age"]} years old")


introduce(name="Levi", age=21)
introduce(name="Zikirullo", age=21, single=True)

print('=== args & kwargs ===')


def greet(*args, **kwargs):
    print("*args", args)
    print(f"**kwargs", kwargs)


greet("hi", True, name="John", age=27)

print('=== zip ===')
tuple1 = (1, 2, 3, 4)
tuple2 = ("a", "b", "c")
zipped = zip(tuple1, tuple2)
print(zipped)
result = list(zipped)
print(result)
