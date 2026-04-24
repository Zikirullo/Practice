print('=== For ===')

'''
Iterable objects: string, dict, tuple, list, range, map, filter

for operatori odatda, bergilangan tartibda, bergilangan ketmaketlikda aniq bolganda for ishlatiladi, 
while esa takrorlanishlar tartibi no'malum boganda ishlatiladi. 
'''
text = "MIT"
numbers = [10, 5, 4, 1]
car_obj = dict(brand="Tesla", year=2025)
range_obj = range(5)

for letter in text:
    print(f"the letters {letter}")

print('-'*10)
for numb in numbers:
    print(f"the numbers {numb}")

print('-'*10)
for x in range_obj:
    print(f"ranging {x}")

print('-'*10)
for cars in car_obj:
    print(f"the key: {cars} => the value: {car_obj.get(cars)}")

for y in range(1, 20, 5):  # start in 1 and keep adding 5 until you reach 20
    print(f"{y}")

print('=== break/else ===')
for x in range(1, 20, 5):
    print(x)
    if x > 100:
        print('you reached the limit')
        break
else:
    print('Succecfully looped')


print("=== while ===")

number = 40
while number > 0:
    number -= 10
    print(f"{number}")

count = 0
while True:
    count += 1
    x = int(input("Find a number"))

    if x == 41:
        print(f"you found the number in {count} steps")
        break
    else:
        print("Wrong! please try again")
