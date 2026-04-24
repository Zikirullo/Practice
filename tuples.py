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
