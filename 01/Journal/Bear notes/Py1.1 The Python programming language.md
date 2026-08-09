# Py1.1 The Python programming language
The programming language you will be learning is Python. Python is an example of a **high-level language**; other high-level languages you might have heard of are C++, PHP, Pascal, C#, and Java.

As you might infer from the name high-level language, there are also ::low-level languages::, sometimes referred to as machine languages or assembly languages. Loosely speaking, computers can only execute programs written in low-level languages. Thus, programs written in a high-level language have to be translated into something more suitable before they can run.

Almost all programs are written in high-level languages because of their advantages. It is ~much easier to program~ in a high-level language so programs take less time to write, they are shorter and easier to read, and they are more likely to be correct. Second, high-level languages are ~portable~, meaning that they can run on different kinds of computers with few or no modiﬁcations.

The engine that translates and runs Python is called the **Python Interpreter**: There are two ways to use it: ~immediate mode~ and ~script mode~. In immediate mode, you type Python expressions into the Python Interpreter window, and the interpreter immediately shows the result:
![](Py1.1%20The%20Python%20programming%20language/Attachment.png)

The **>>>** is called the ~Python prompt~. The interpreter uses the prompt to indicate that it is ready for instructions. We typed 2 + 2, and the interpreter evaluated our expression, and replied 4, and on the next line it gave a new prompt, indicating that it is ready for more input.

Alternatively, you can write a program in a ﬁle and use the interpreter to execute the contents of the ﬁle. Such a ﬁle is called a script. Scripts have the advantage that they can be saved to disk, printed, and so on.

In this Rhodes Local Edition of the textbook, we use a program development environment called PyScripter. (It is available at http://code.google.com/p/pyscripter.) There are various other development environments. If you’re using one of the others, you might be better off working with the authors’ original book rather than this edition.

For example, we created a ﬁle named firstprogram.py using PyScripter. By convention, ﬁles that contain Python programs have names that end with .py

To execute the program, we can click the Run button in PyScripter:
![](Py1.1%20The%20Python%20programming%20language/Attachment%202.png)
Most programs are more interesting than this one.

Working directly in the interpreter is convenient for testing short bits of code because you get immediate feedback. Think of it as scratch paper used to help you work out problems. Anything longer than a few lines should be put into a script.

#code/python