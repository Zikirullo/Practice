print('=== What is comprehension & list comprehension ===')
# It acts like a spread operator of other stacks

''' Comprehension general syntax:
A) * itarable
B) <expression> for item in iterable
C) <expression> for item in iterable <condition>
'''
# LIST COMPREHENSION
numbers = [1, 2, 6, 4, 2, 10]
list_num = [*numbers]
print("list_num:", list_num)

print("-------------------")

people = [
    ("Zikirullo", 21),
    ("Levy", 27),
    ("Deen", 22),
]
list_people = [person[1] for person in people]
print("list_people:", list_people)


cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33),
]
list_cars = [car[0] for car in cars if car[1] > 80]
print("list_cars:", list_cars)

print("✅"*20)
print("")
print("=== SET and DICTINARY comprehension ===")
print("")

numbs = [3, 44, 51, 4, 32, 4, 3, 5, 1, 4, 2, 4, 5, 44]
set_numbers = {*numbs}
print("SET_numbers:", set_numbers)
print('')

dict_people = {person[0]: person[1] for person in people}
print("DICTINARY_people:", dict_people)
print("")

dict_people = {person[0] for person in people if person[1] <= 21}
print("dict_people:", dict_people)
print("")
