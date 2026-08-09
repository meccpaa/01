# Py2.7 Type converter functions
Here we’ll look at three more Python functions, int, float and str, which will (attempt to) convert their arguments into types int, float and str respectively. We call these type converter functions.

The int function can take a ﬂoating point number or a string, and turn it into an int. For ﬂoating point numbers, it discards the decimal portion of the number — a process we call truncation towards zero on the number line. Let us see this in action:
```
>>> int(3.14) 
3
>>> int(3.9999)  # This doesn’t round to the closest int!
3
>>> int(3.0) 
3
>>> int(-3.999) # Note that the result is closer to zero
-3
>>> int(minutes / 60) 
10
>>> int("2345")  # Parse a string to produce an int
2345
>>> int(17) # It even works if arg is already an int
17
>>> int("23 bottles")
```
This last case doesn’t look like a number — what do we expect?
```
Traceback (most recent call last):
File "<interactive input>", line 1, in <module> 
ValueError: invalid literal for int() with base 10: ’23 bottles’
```
The type converter float can turn an integer, a ﬂoat, or a syntactically legal string into a ﬂoat:
```
>>> float(17)
17.0
>>> float("123.45")
123.45
```
The type converter str turns its argument into a string:
```
>>> str(17) 
’17’
>>> str(123.45) 
’123.45’
```
#code/python