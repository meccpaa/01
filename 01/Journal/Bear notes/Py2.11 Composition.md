# Py2.11 Composition
So far, we have looked at the elements of a program — variables, expressions, statements, and function calls — in isolation, without talking about how to combine them.

One of the most useful features of programming languages is their ability to take small building blocks and compose them into larger chunks.

For example, we know how to get the user to enter some input, we know how to convert the string we get into a ﬂoat, we know how to write a complex expression, and we know how to print values. Let’s put these together in a small four-step program that asks the user to input a value for the radius of a circle, and then computes the area of the circle from the formula
![](Py2.11%20Composition/A142CCD0-DB7C-487D-B4F2-9D585B6446A6.png)
Firstly, we’ll do the four steps one at a time:
```
response = input("What is your radius? ") 
r = float(response) 
area = 3.14159 * r ** 2 
print("The area is ", area)
```
Now let’s compose the ﬁrst two lines into a single line of code, and compose the second two lines into another line of code.
```
r = float( input("What is your radius? ") ) 
print("The area is ", 3.14159 * r ** 2)
```
If we really wanted to be tricky, we could write it all in one statement:
`print("The area is ", 3.14159 * float(input("What is your radius?")) ** 2)`
Such compact code may not be most understandable for humans, but it does illustrate how we can compose bigger chunks from our building blocks.

If you’re ever in doubt about whether to compose code or fragment it into smaller steps, try to make it as simple as you can for the human to follow. My choice would be the ﬁrst case above, with four separate steps.

#code/python