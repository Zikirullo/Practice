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

print("=== Conditions ==="*6)

x = 21
if x > 50:
    print("Case A")
elif x > 20:
    print("Case B")
else:
    print('Case C')

age = 21
# Person = None

# if age > 16:
#     person = "young-adult"
# else:
#     person = "child"

# print(person)

# Ternary
person = "young-adult" if age > 18 else "child"
print(person)

is_Student = True
is_Admin = True
is_Host = True
is_Parent = False

if is_Parent:
    print('Do you wanna be a parent')
elif not is_Admin:
    print('Please go the office and work')
# at least one case is true, => TRUE but in (and) operator every case is true => TRUE, al least one case is false => FALSE
elif is_Host or is_Student:
    print("Waiting room is over there")
else:
    print("WHO ARE YOU?")
