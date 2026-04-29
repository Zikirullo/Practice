from PIL import Image
import turtle
print("=== Python packages & core packages ===")

'''
There are three type of modules/packages in python: core, file, external
'''
t = turtle.Turtle()
t.shape("turtle")
t.speed(2)
t.circle(150)

turtle.done

# By the following approach we have to open and close every file we add.

my_life = open("material/message.txt", "r")
try:
    content = my_life.read()
    print("content:", content)
finally:
    my_life.close()

with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("=== Package manager & External packages ===")
# Package manager for PYTHON: pip, pipenv
# Package manager for NODEJS: npm yarn

with Image.open("material/logo.jpg") as img_obj:
    resize = img_obj.resize((200, 200))
    resize.show()
    resize.save("material/result.jpg")

print("=== Debugging ===")


def get(*args):
    total = 0
    for a in args:
        total += a
        return total  # debugging


result = get(1, 2, 3, 4, 5)
print(result)
