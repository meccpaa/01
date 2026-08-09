# Py3.1 Our first turtle program
Let’s write a couple of lines of Python program to create a new turtle and start drawing a rectangle. (We’ll call the variable that refers to our ﬁrst turtle alex, but we can choose another name if we follow the naming rules from the previous chapter).

```
import turtle 			# Allows us to use turtles
wn = turtle.Screen() 	 # Creates a playground for turtles
alex = turtle.Turtle()	# Create a turtle, assign to alex

alex.forward(50) 		# Tell alex to move forward by 50 units
alex.left(90) 			 # Tell alex to turn by 90 degrees
alex.forward(30)		# Complete the second side of a rectangle

wn.mainloop()		# Wait for user to close window
```

When we run this program, a new window pops up:
![](Py3.1%20Our%20first%20turtle%20program/FD5420E3-D208-4666-BA8D-98BB8575999B.png)
Here are a couple of things we’ll need to understand about this program.

The **ﬁrst line** tells Python to load a module named turtle. That module brings us two new types that we can use: the Turtle type, and the Screen type. The dot notation turtle.Turtle means “The Turtle type that is deﬁned within the turtle module”. (Remember that Python is ::case sensitive::, so the module name, with a lowercase “t”, is different from the type Turtle.)

We **then** create and open what it calls a screen (we would prefer to call it a window), which we assign to variable “wn”. Every window contains a canvas, which is the area inside the window on which we can draw.

In **line 3** we create a turtle. The variable “alex” is made to refer to this turtle.

So these ﬁrst three lines have set things up, we’re ready to get our turtle to draw on our canvas.

In **lines 5-7**, we instruct the object alex to move, and to turn. We do this by invoking, or activating, alex‘s methods — these are the instructions that all turtles know how to respond to.

The last line plays a part too: the wn variable refers to the window shown above. When we invoke its mainloop method, it enters a state where it waits for events (like keypresses, or mouse movement and clicks). The program will terminate when the user closes the window.

An object can have various methods — things it can do — and it can also have attributes — (sometimes called properties). For example, each turtle has a color attribute. The method invocation `alex.color("red")` will make alex red, and drawing will be red too. (Note the word color is spelled the American way!)

The color of the turtle, the width of its pen, the position of the turtle within the window, which way it is facing, and so on are all part of its current state. Similarly, the window object has a background color, and some text in the title bar, and a size and position on the screen. These are all part of the state of the window object.

Quite a number of methods exist that allow us to modify the turtle and the window objects. We’ll just show a couple. In this program we’ve only commented those lines that are different from the previous example (and we’ve used a different variable name for this turtle):

```
import turtle 
wn = turtle.Screen()
wn.bgcolor("lightgreen") 	# Set the window background color
wn.title("Hello, Tess!")		# Set the window title

tess = turtle.Turtle() 
tess.color("blue") 		# Tell tess to change her color
tess.pensize(3)			# Tell tess to set her pen width

tess.forward(50) 
tess.left(120) 
tess.forward(50)

wn.mainloop()
```
When we run this program, this new window pops up, and will remain on the screen until we close it.
- - - -
## Extend this program ...
1. Modify this program so that before it creates the window, it prompts the user to enter the desired background color. It should store the user’s responses in a variable, and modify the color of the window according to the user’s wishes. (Hint: you can ﬁnd a list of permitted color names at http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm. It includes some quite unusual ones, like “peach puff” and “HotPink”.)

2. Do similar changes to allow the user, at runtime, to set tess‘ color.

3. Do the same for the width of tess‘ pen. Hint: your dialog with the user will return a string, but tess‘ pensize method expects its argument to be an int. So you’ll need to convert the string to an int before you pass it to pensize.

#code/python