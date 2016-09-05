#### 1. Exercise 3.3 from thinkPython:
Exercise 3.3. Python provides a built-in function called len that returns the length of a string.
So len(‘allen’) = 5, len(‘darwyn’) = 6. Note that len works on many objects, not just strings.

Think of the screen on your computer as having 70 columns, each of which can contain a letter, number, punctuation, etc. Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

```
def right_justify(s):

     <your code goes here>

right_justify(‘Allen’)
right_justify(‘Python is amazing’)

Output:
                                                                                                         Allen
                                                                                             Python is amazing
```

####2. Exercise 3.5 from thinkPython
Exercise 3.5. Write a procedure box() that prints a grid. There should be a line with "+" and "-"' followed by four lines with "|" and blanks, followed by another line like the first followed by four lines with "|" and blanks followed by another line like the first. See the picture below.

You should have two different functions to print out the rows, and another function which calls these to print out the box. horizontal(x) will be used to print the lines with "+" and "-", vertical(x) will print the lines "|" and blanks. The x is the total number of characters in the row. In the example below x is 11, so that we kno

x is the width of the row
```
def horizontal(x)
     <your code goes here>
def vertical(x)
     <your code goes here>
def box(x)
     <your code goes here>
horizontal(11)
print("\n")
vertical(11)
print("\nYour box should look like:\n")
box(11)
Output
+----+----+

|    |    |

Your box should look like:

+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+
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

#### 4. Create a knockknock(answer, punchline) procedure that accepts two inputs, the answer to who’s there and the punchline, and prints out the knock knock joke. 

Your program should call knockknockintro() and setup().

knockknock("Canoe", "help me with my homework?") should print out

Knock, knock
Who's there?
Canoe
Canoe who?
Canoe help me with my homework?

