import turtle
print("=== Python packages & core packages ===")

'''
There are three type of modules/packages in python: core, file, external
'''
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(150)

# turtle.done

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
