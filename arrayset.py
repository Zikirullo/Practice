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
