print('=== What is comprehension & list comprehension ===')
# It acts like a spread operator of other stacks

''' Comprehension general syntax:
01. * itarable
02. <expression> for item in iterable
03. <expression> for item in iterable <condition>
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
