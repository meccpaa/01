# Py3.3 The for loop
When we drew the square, it was quite tedious. We had to explicitly repeat the steps of moving and turning four times. If we were drawing a hexagon, or an octogon, or a polygon with 42 sides, it would have been worse.

So a basic building block of all programs is to be able to repeat some code, over and over again.

Python’s `for` loop solves this for us. Let’s say we have some friends, and we’d like to send them each an email inviting them to our party. We don’t quite know how to send email yet, so for the moment we’ll just print a message for each friend:

```
for f in ["Joe","Zoe","Brad","Angelina","Zuki","Thandi","Paris"]:
	invite = "Hi " + f + ". Please come to my party on Saturday!"
	print(invite) 
‘# more code can follow here ...
```

When we run this, the output looks like this:
> Hi Joe. Please come to my party on Saturday!  
> Hi Zoe. Please come to my party on Saturday!  
> Hi Brad. Please come to my party on Saturday!  
> Hi Angelina. Please come to my party on Saturday!   
> Hi Zuki. Please come to my party on Saturday!  
> Hi Thandi. Please come to my party on Saturday!   
> Hi Paris. Please come to my party on Saturday!  

• The variable f in the for statement at line 1 is called the loop variable. We could have chosen any other variable name instead.
• Lines 2 and 3 are the loop body. The loop body is always indented. The indentation determines exactly what statements are “in the body of the loop”.
• On each iteration or pass of the loop, ﬁrst a check is done to see if there are still more items to be processed. If there are none left (this is called the terminating condition of the loop), the loop has ﬁnished. Program execution continues at the next statement after the loop body, (e.g. in this case the next statement below the comment in line 4).
• If there are items still to be processed, the loop variable is updated to refer to the next item in the list. This means, in this case, that the loop body is executed here 7 times, and each time f will refer to a different friend.
• At the end of each execution of the body of the loop, Python returns to the for statement, to see if there are more items to be handled, and to assign the next one to f.

#code/python