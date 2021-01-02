def right_justify(s):
    s = (" "*(70-len(s))+s)
    print(s)


right_justify("Allen")
right_justify("Python is amazing!")


def line(x):
    x = "+"+("-"*((x-3)/2))+"+"+("-"*((x-3)/2))+"+"
    print(x)


line(5)
line(9)
line(25)
