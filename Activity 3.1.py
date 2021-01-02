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


def box(x):
    x = int((x-3)/2)
    y = "+"+("-"*x)+"+"+("-"*x)+"+"
    z = "|"+(" "*x)+"|"+(" "*x)+"|"
    print(y+"\\n"+(z*4)+"\\n"+y+"\\n"+(z*4)+"\\n"+y)


box(11)
print("\\n\\n")
box(5)
