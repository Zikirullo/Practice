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
