# Py3.6 A few more turtle methods and tricks
Turtle methods can use negative angles or distances. So tess.forward(-100) will move tess backwards, and tess.left(-30) turns her to the right. Additionally, because there are 360 degrees in a circle, turning 30 to the left will get tess facing in the same direction as turning 330 to the right! (The on-screen animation will differ, though — you will be able to tell if tess is turning clockwise or counter-clockwise!)

This suggests that we don’t need both a left and a right turn method — we could be minimalists, and just have one method. There is also a backward method. (If you are very nerdy, you might enjoy saying alex.backward(-100) to move alex forward!)

Part of thinking like a scientist is to understand more of the structure and rich relationships in our ﬁeld. So revising a few basic facts about geometry and number lines, and spotting the relationships between left, right, backward, forward, negative and positive distances or angles values is a good start if we’re going to play with turtles.

A turtle’s pen can be picked up or put down. This allows us to move a turtle to a different place without drawing a line. The methods are
```
alex.penup() 
alex.forward(100) 	# This moves alex, but no line is drawn
alex.pendown()
```
Every turtle can have its own shape. The ones available “out of the box” are arrow, blank, circle, classic, square, triangle, turtle.

`alex.shape("turtle")`
![](Py3.6%20A%20few%20more%20turtle%20methods%20and%20tricks/0B360B7C-68F3-418E-9D98-9DC25C8362AA.png)

We can speed up or slow down the turtle’s animation speed. (Animation controls how quickly the turtle turns and moves forward). Speed settings can be set between 1 (slowest) to 10 (fastest). But if we set the speed to 0, it has a special meaning — turn off animation and go as fast as possible.

alex.speed(10)

A turtle can “stamp” its footprint onto the canvas, and this will remain after the turtle has moved somewhere else. Stamping works, even when the pen is up.

Let’s do an example that shows off some of these new features:

`import turtle `
`wn = turtle.Screen() `
`wn.bgcolor("lightgreen") `
`tess = turtle.Turtle() `
`tess.shape("turtle") `
`tess.color("blue")`

`tess.penup() 		# This is new`
`size = 20`
`for i in range(30):`
`	tess.stamp() 			# Leave an impression on the canvas`
`	size = size + 3 		# Increase the size on every iteration`
`	tess.forward(size)		# Move tess along`
`	tess.right(24) 		# … and turn her`

`wn.mainloop()`

![](Py3.6%20A%20few%20more%20turtle%20methods%20and%20tricks/EF5BC9A7-D2EC-4D59-801E-9501F9BC1ED2.png)
Be careful now! How many times was the body of the loop executed? How many turtle images do we see on the screen? All except one of the shapes we see on the screen here are footprints created by stamp. But the program still only has one turtle instance — can you ﬁgure out which one here is the real tess? (Hint: if you’re not sure, write a new line of code after the for loop to change tess‘ color, or to put her pen down and draw a line, or to change her shape, etc.)

#code/python