# Py3.2 Instances - a herd of turtles
Just like we can have many different integers in a program, we can have many turtles. Each of them is called an instance. Each instance has its own attributes and methods — so alex might draw with a thin black pen and be at some position, while tess might be going in her own direction with a fat pink pen.

```
import turtle 
wn = turtle.Screen() 
wn.bgcolor("lightgreen") 
wn.title("Tess & Alex")

tess = turtle.Turtle() 
tess.color("hotpink") 
tess.pensize(5)

alex = turtle.Turtle()

tess.forward(80) 
tess.left(120) 
tess.forward(80) 
tess.left(120) 
tess.forward(80) 
tess.left(120)

tess.right(180) 
tess.forward(80)

alex.forward(50) 
alex.left(90) 
alex.forward(50) 
alex.left(90) 
alex.forward(50) 
alex.left(90) 
alex.forward(50) 
alex.left(90)

wn.mainloop()
```

Here is what happens when alex completes his rectangle, and tess completes her triangle:
![](Py3.2%20Instances%20-%20a%20herd%20of%20turtles/18E57961-82B2-46E0-8DAE-B28E09C93BB5.png)
Here are some How to think like a computer scientist observations:
• There are 360 degrees in a full circle. If we add up all the turns that a turtle makes, no matter what steps occurred between the turns, we can easily ﬁgure out if they add up to some multiple of 360. This should convince us that alex is facing in exactly the same direction as he was when he was ﬁrst created. (Geometry conventions have 0 degrees facing East, and that is the case here too!)

• We could have left out the last turn for alex, but that would not have been as satisfying. If we’re asked to draw a closed shape like a square or a rectangle, it is a good idea to complete all the turns and to leave the turtle back where it started, facing the same direction as it started in. This makes reasoning about the program and composing chunks of code into bigger programs easier for us humans!

• We did the same with tess: she drew her triangle, and turned through a full 360 degrees. Then we turned her around and moved her aside. Even the blank line 18 is a hint about how the programmer’s mental chunking is working: in big terms, tess‘ movements were chunked as “draw the triangle” (lines 12-17) and then “move away from the origin” (lines 19 and 20).

• One of the key uses for comments is to record our mental chunking, and big ideas.

They’re not always explicit in the code.

• And, uh-huh, two turtles may not be enough for a herd. But the important idea is that the turtle module gives us a kind of factory that lets us create as many turtles as we need. Each instance has its own state and behaviour.

#code/python