print("=== Iterable objects ===")
'''
Iterable objects: string, dict, tuple, list, range, map, filter
'''
text = "MIT"

range_obj = range(3)
print("range_obj:", range_obj)

for letter in text:
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element {ele}")

print("=== Dictionary ===")
# Dictionary is also can be called JSON object.

person = {
    "name": "Justin",
    "age": 25,
    "single": True
}
#                 OR
person1 = dict(
    name="Levi",
    age=21,
    single=True)

print(f"the person: {person}")
print(f"the person1: {person1}")

# if we need to take one key out of the object
name = person1["name"]
print("THE NAME:", name)
# if there is no specific key that we search for, python gives an error.

age = person1.get("age")
print("THE AGE:", age)

# but, if we use get() method for the key that doesn't exist, python gives NONE.
hobby = person1.get("hobby")
print("THE HOBBY:", hobby)

balance = person1.get("the person1", "$100")
print(f"the name: {name}, the age: {age}, balance: {balance}")

for key in person1:
    print(f"the key: {key} => value {person1[key]}")

del person["single"]
print(person)
