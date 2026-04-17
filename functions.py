'''Function learning:
01. Define va Call 
02. Parament va Argument
03. Keyword va default arguments
04. Scope
'''
print("=== Define va Call")

# Define


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greetin is exeuted")
    return f"HI {b}"

    # Call
greet("Zikirullo")

result1 = greet("Zikirullo")
print("result1:", result1)  # None

result2 = greeting("Levi")
print("result2:", result2)

print("=== keyword & default arguments ===")


def giveGreet(name, age):
    print("giveGreet is executed")
    return f"Hi {name}, you're {age} years old"


result3 = giveGreet(name="Zikirullo", age=21)
print("result3:", result3)


def defaultGreet(name, age=21):
    print("giveGreet is executed")
    return f"Hi {name}, you're {age} years old"


result4 = defaultGreet("Levi")
print("result3:", result4)
