# Py3.5 The loop simplifies our turtle program
To draw a square we’d like to do the same thing four times — move the turtle, and turn. We previously used 8 lines to have alex draw the four sides of a square. This does exactly the same, but using just three lines:
```
for i in [0,1,2,3]:
	alex.forward(50) 
	alex.left(90)
```

Some observations:
• While “saving some lines of code” might be convenient, it is not the big deal here. What is much more important is that we’ve found a “repeating pattern” of statements, and reorganized our program to repeat the pattern. Finding the chunks and somehow getting our programs arranged around those chunks is a vital skill in computational thinking.
• The values [0,1,2,3] were provided to make the loop body execute 4 times. We could have used any four values, but these are the conventional ones to use. In fact, they are so popular that Python gives us special built-in range objects:

```
for i in range(4):
‘# Executes the body with i = 0, then 1, then 2, then 3 

for x in range(10):
‘# Sets x to each of ... [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

• Computer scientists like to count from 0!
• range can deliver a sequence of values to the loop variable in the for loop. They start at 0, and in these cases do not include the 4 or the 10.
• Our little trick earlier to make sure that alex did the ﬁnal turn to complete 360 degrees has paid off: if we had not done that, then we would not have been able to use a loop for the fourth side of the square. It would have become a “special case”, different from the other sides. When possible, we’d much prefer to make our code ﬁt a general pattern, rather than have to create a special case.

So to repeat something four times, a good Python programmer would do this:
```
for i in range(4):
	alex.forward(50) 
	alex.left(90)
```
By now you should be able to see how to change our previous program so that tess can also use a for loop to draw her equilateral triangle.

But now, what would happen if we made this change?
```
for c in ["yellow", "red", "purple", "blue"]:
	alex.color(c) 
	alex.forward(50) 
	alex.left(90)
```
A variable can also be assigned a value that is a list. So lists can also be used in more general situations, not only in the for loop. The code above could be rewritten like this:
```
‘# Assign a list to a variable 
clrs = ["yellow", "red", "purple", "blue"] 
for c in clrs:
	alex.color(c) 
	alex.forward(50) 
	alex.left(90)
```

#code/python