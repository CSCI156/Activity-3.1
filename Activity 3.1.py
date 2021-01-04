def right_justify(s):
    s = (" "*(70-len(s))+s)
    print(s)


right_justify("Allen")
right_justify("Python is amazing!")


def line(x):
    x = int((x-3)/2)
    y = "+"+("-"*x)+"+"+("-"*x)+"+"
    print(y)


line(5)
line(9)
line(25)


def horizontal(x):
    x = int((x-3)/2)
    y = "|"+(" "*x)+"|"+(" "*x)+"|"
    print(y)


horizontal(5)
horizontal(9)
horizontal(25)
print("\n\n")


def box(x):
    x = int((x-3)/2)
    y = "+"+("-"*x)+"+"+("-"*x)+"+"
    z = "|"+(" "*x)+"|"+(" "*x)+"|"+"\n"
    print(y+"\n"+(z*4)+y+"\n"+(z*4)+y)


box(11)
print("\n\n")
box(5)

print("\n")


def knockknockintro():
    print("Knock, knock")
    print("Who’s there?")


def setup(x):
    x = x+"\n"+(x+" "+"who?")
    print(x)


knockknockintro()
setup("canoe")
print("\n")


def knockknock(x, y):
    z = "Knock knock"+"\n"+"Who's there?"+"\n"
    x = x
    w = x+" "+"who?"+"\n"
    y = x+" "+y
    print(z+x+"\n"+w+y)


knockknock("Canoe", "help me with my homework?")
print("\n")
knockknock("Boo", "don't cry it's just a joke!")
