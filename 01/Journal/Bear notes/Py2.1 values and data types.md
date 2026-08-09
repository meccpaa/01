# Py2.1 values and data types
A value is one of the fundamental things — like a letter or a number — that a program manipulates. The values we have seen so far are `4` (the result when we added `2 + 2`), and "`Hello, World!`".

These values are classiﬁed into different **classes**, or **data types**: `4` is an *integer*, and "`Hello, World!`" is a *string*, so-called because it contains a string of letters. You (and the interpreter) can identify strings because they are enclosed in quotation marks.

If you are not sure what class a value falls into, Python has a function called **type** which can tell you.

```
>>> type("Hello, World!") 
<class ’str’>
>>> type(17) 
<class ’int’>
```

Not surprisingly, strings belong to the class **str** and integers belong to the class **int**. Less obviously, numbers with a decimal point belong to a class called **ﬂoat**, because these numbers are represented in a format called ~ﬂoating-point~. At this stage, you can treat the words class and type interchangeably. We’ll come back to a deeper understanding of what a class is in later chapters.

```
>>> type(3.2) 
<class ’float’>
```

What about values like `"17"` and `"3.2"`? They look like numbers, but they are in quotation marks like strings.

```
>>> type("17") 
<class ’str’>
>>> type("3.2") 
<class ’str’>
```

They’re strings!

Strings in Python can be enclosed in either single quotes (’) or double quotes ("), or three of each (”’ or """)

```
>>> type(’This is a string.’) 
<class ’str’>
>>> type("And so is this.") 
<class ’str’>
>>> type("""and this.""") 
<class ’str’>
>>> type(’’’and even this...’’’) 
<class ’str’>
```

Double quoted strings can contain single quotes inside them, as in `"Bruce’s beard"`, and single quoted strings can have double quotes inside them, as in `’The knights who say "Ni!"’`.

Strings enclosed with three occurrences of either quote symbol are called triple quoted strings. They can contain either single or double quotes:
```
>>> print(’’’"Oh no", she exclaimed, "Ben’s bike is broken!"’’’) "Oh no", she exclaimed, "Ben’s bike is broken!"
>>>
```

Triple quoted strings can even span multiple lines:
```
>>> message = """This message will 
... span several 
... lines."""
>>> print(message) 
This message will 
span several 
lines.
>>>
```
Python doesn’t care whether you use single or double quotes or the three-of-a-kind quotes to surround your strings: once it has parsed the text of your program or command, the way it stores the value is identical in all cases, and the surrounding quotes are not part of the value. But when the interpreter wants to display a string, it has to decide which quotes to use to make it look like a string.
```
>>> ’This is a string.’ 
’This is a string.’
>>> """And so is this.""" 
’And so is this.’
```
So the Python language designers usually chose to surround their strings by single quotes. What do think would happen if the string already contained single quotes?

When you type a large integer, you might be tempted to use commas between groups of three digits, as in `42,000`. This is not a legal integer in Python, but it does mean something else, which is legal:
```
>>> 42000 
42000
>>> 42,000 
(42, 0)
```
Well, that’s not what we expected at all! Because of the comma, Python chose to treat this as a pair of values. We’ll come back to learn about pairs later. But, for the moment, remember not to put commas or spaces in your integers, no matter how big they are. Also revisit what we said in the previous chapter: formal languages are strict, the notation is concise, and even the smallest change might mean something quite different from what you intended.

#code/python