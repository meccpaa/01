# Py2.12 The modulus operator
The modulus operator works on integers (and integer expressions) and gives the remainder when the ﬁrst number is divided by the second. In Python, the modulus operator is a percent sign (%). The syntax is the same as for other operators. It has the same precedence as the multiplication operator.

>>> q = 7 // 3 # This is integer division operator
>>> print(q) 
2
>>> r = 7 % 3
>>> print(r) 
1

So 7 divided by 3 is 2 with a remainder of 1.

The modulus operator turns out to be surprisingly useful. For example, you can check whether one number is divisible by another—if x % y is zero, then x is divisible by y.

Also, you can extract the right-most digit or digits from a number. For example, x % 10 yields the right-most digit of x (in base 10). Similarly x % 100 yields the last two digits.

It is also extremely useful for doing conversions, say from seconds, to hours, minutes and seconds. So let’s write a program to ask the user to enter some seconds, and we’ll convert them into hours, minutes, and remaining seconds.
```
total_secs = int(input("How many seconds, in total?")) 
hours = total_secs // 3600 
secs_still_remaining = total_secs % 3600 
minutes = secs_still_remaining // 60 
secs_finally_remaining = secs_still_remaining % 60
print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
```
#code/python