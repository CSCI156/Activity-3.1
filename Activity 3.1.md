#### 1. Exercise 3.3 from thinkPython:
Exercise 3.3. Python provides a built-in function called len that returns the length of a string.
So len(‘allen’) = 5, len(‘darwyn’) = 6. Note that len works on many objects, not just strings.

Think of the screen on your computer as having 70 columns, each of which can contain a letter, number, punctuation, etc. Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

```
def right_justify(s):

     <your code goes here>

right_justify(‘allen’)
right_justify(‘Python is amazing’)

Output:
                                                                                                         allen
                                                                                             Python is amazing
```

####2. Exercise 3.5 from thinkPython
Exercise 3.5. This exercise can be done using only the statements and other features we have learned
so far.
1. Write a function that draws a grid like the following:
You should have two different functions to print out the rows, and another functions which calls these to print out the box.

x is the width of the row
```
def horizontal(x)
     <your code goes here>
def vertical(x)
     <your code goes here>
def box(x)
     <your code goes here>
horizontal(11)
vertical(11)
box(11)
Output
+ - - - - + - - - - +
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
```

#### 3. Here is the code for version 3 of knockknock:
```
def knockknockintro():
     print("Knock, knock")
     print("Who’s there?")

knockknockintro()
print("Canoe. \nCanoe who?\nCanoe help me with my homework?\n")
```

Add a procedure called setup that will take an input x, which is a string, and print out that string followed by a 
new line with string and who?

for example  setup(“Iva”)  will print out
Iva
Iva who?

#### 4. Create a knockknock procedure that accepts two inputs, the answer to who’s there and the punchline, and prints out the
knock knock joke. Your program should call knockknockintro()  and setup().

