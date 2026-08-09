# Py2.6 Operators and operands
Operators are special tokens that represent computations like addition, multiplication and division. The values the operator uses are called operands.

The following are all legal Python expressions whose meaning is more or less clear:

`20+32`  `hour-1` `hour * 60+minute` `minute/60` `5 ** 2` `(5+9) * (15-7)`

The tokens +, -, and * , and the use of parenthesis for grouping, mean in Python what they mean in mathematics. The asterisk ( * ) is the token for multiplication, and ** is the token for exponentiation.
```
>>> 2 ** 3 
8
>>> 3 ** 2 
9
```
When a variable name appears in the place of an operand, it is replaced with its value before the operation is performed.

Addition, subtraction, multiplication, and exponentiation all do what you expect.

Example: so let us convert 645 minutes into hours:
```
>>> minutes = 645
>>> hours = minutes / 60
>>> hours
10.75
```
Oops! In Python 3, the division operator / always yields a ﬂoating point result. What we might have wanted to know was how many whole hours there are, and how many minutes remain. Python gives us two different ﬂavors of the division operator. The second, called ﬂoor division uses the token //. Its result is always a whole number — and if it has to adjust the number it always moves it to the left on the number line. So 6 // 4 yields 1, but -6 // 4 might surprise you!
```
>>> 7 / 4
1.75
>>> 7 // 4 
1
>>> minutes = 645
>>> hours = minutes // 60
>>> hours 
10
```
Take care that you choose the correct ﬂavor of the division operator. If you’re working with expressions where you need ﬂoating point values, use the division operator that does the division accurately.

#code/python