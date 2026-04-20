import array  # module/package
import math
from math import ceil, asin
print("=== what is oblect ===")
# Object has state and properties
# Evetything is an object in Python

print(type('hello world!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

result1 = math.ceil(97.7)  # CALL
print(result1)

result2 = ceil(98.7)
print(result2)

print("=== Error handling system ===")

car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("passed here")
    change = car_dict.speed
    result = car_dict["origin "]
    print("result")
except KeyError as err:
    print("No data for origin was found, please try again", err)
except AttributeError as err:
    print("whatever you're asking there's no data for that")
else:
    print("Executec successfully without an error")
finally:
    print("Final closing logic")
# else mantig'i qachonki try: da error bolmasa ishga tushadi. finally esa xar doim ishga tushadi, eng oxiridda.
