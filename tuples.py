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
