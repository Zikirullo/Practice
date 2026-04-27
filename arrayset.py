from array import array
# Judda katta hajmdagi malumotlar uchun array ni ishlatamiz
print('=== Array ===')

numbers = array("i", [1, 3, 5, 7, 9, 8, 6, 4, 2])
numbers.append(100)
numbers.insert(2, 200)
print(numbers)

numbers.remove(5)
numbers.pop()

del numbers[0:2]
print(numbers)

print('=== SET ===')

numbers = array("i", [1, 3, 5, 3, 7, 9, 8, 1, 6, 4, 2])
new = set(numbers)
print(new)

new.add(200)
print(new)

new.add(3)
print(new)

print('=== Specific operators with SET ===')
print("✅"*20)


# |, &, -, ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union
result2 = a & b  # intersection
result3 = a - b  # difference
result4 = a ^ b  # symmetric difference
print("Union", result1)
print("Intersection", result2)
print("Difference", result3)
print("Symmetric difference", result4)
