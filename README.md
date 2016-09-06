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
Exercise 3.5. 
<br>
i. Write a procedure horizontal(x) that prints a line that is a "+" followed by some dashes followed by a "+" followed by the same number of dashes followed by a "+". The number of dashes is determined by x, which is the total number of characters on the line

Examples with output:
```
horizontal(5)
horizontal(9)
horizontal(25)
Output:
+-+-+
+---+---+
+-----------+-----------+
```

ii. Write a procedure vertical(x) that prints a line that is a "|" followed by some spaces followed by a "|" followed by the same number of spaces followed by a "|". The number of spaces is determined by x, which is the total number of characters on the line.
```
horizontal(5)
Output:
| | |
horizontal(9)
Output:
|   |   |
horizontal(25)
Output:
|           |           |
```

iii. Write a procedure box(x) which uses vertical(x) and horizontal(x) to print a box that has width x. There should be a horizontal row, followed by four vertical rows, followed by another horizontal row, four vertical rows, and finally a horizontal row all of width x. 

```
def box(x)
     <your code goes here>
     
box(11)
print("\n\n")
box(5)
Output:
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


+-+-+
| | |
| | |
| | |
| | |
+-+-+
| | |
| | |
| | |
| | |
+-+-+
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
<br>
Iva who?

#### 4. Create a knockknock(answer, punchline) procedure that accepts two inputs, the answer to who’s there and the punchline, and prints out the knock knock joke. 

Your program should call knockknockintro() and setup().

knockknock("Canoe", "help me with my homework?") should print out

Knock, knock
<br>
Who's there?
<br>
Canoe
<br>
Canoe who?
<br>
Canoe help me with my homework?
