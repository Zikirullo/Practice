print("=== Operators ===")

a = 19
b = 5
print(a > b)
print(a / b)
print(a * b)

result = a // b  # floor division
left = a % b  # qoldiqlik bolish
print(f' the result: {result} and left: {left}')

# (a = a + 100) = (a += 100)

# a += 100
# print(a)
a = a + 100
print(a)
print(b**2)
print(b**3)

print("="*90)

c = dict(name="Zikirullo", age=21)
d = dict(name="Zikirullo", age=21)
e = c

# Python da ikkta qiymat solishtirilganda ularning reference emas balki valuesi ya'ni qiymati solishtiriladi.

print("c==d:", c == d)

print("c is d", c is d)
print("e is c", e is c)
print(id(c), id(d), id(e))
