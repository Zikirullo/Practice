print("=== number ===")


# In JAVA: Variable is name of storage location!
# In Python: VAriable is named reference since everything in Python have a reference.

count = 100
print(count)
count_type = type(count)
print(count, count_type)
print(f"the count: {count} and type{count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("=== string ===")
# METHOD: upper(), lower(), title(), find(), replace()
print("=== 01 ===")

course = "AI Python FullStack"
result = type(course)
print("the type of the course",  result)

print("=== 03 ===")

result = course.title()
print("The name of the course", result)

print("=== 03 ===")

result = course.upper()
print("the result", result)

print("=== 04 ===")

result = course.replace("FULLSTACK", "MasterClass")
print(f"the result: {result}")

print(result)

print("=== boolean ===")

# functions > type(), input(), bool(), int(), str()
# TRUTHY: true, 100, -100, "MIT"
# FALSY: false, 0, "", NOne

y = input("Give your Valur for y:")
print(y)
result = y.isnumeric()
print(f"the input number is numeric: {result}")

test_falsy = ""
print("The Falsy:", bool(test_falsy))
