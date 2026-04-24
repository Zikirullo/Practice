# part 1
# Dunder: __buitdins__, __init__.

message = ("PYTHON: Everything is object!")
print(message)

result = type(message)
print(result)

'''In Python there are buindin tools:
01.TYPES - int, float, str, list, dict
02.FUNCTION - print(), len(), input(), type()
03.CONSTANS - True, False, None
'''
print(dir(__builtins__))

a = 300
b = 300

print(id(a), id(b))
print(a is b)
