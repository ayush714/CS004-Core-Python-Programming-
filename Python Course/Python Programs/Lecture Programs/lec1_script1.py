"""
Lecture 1 
Date  : 25-09-2021
Course: CS004 ( Core Python )
Topic : Python Basics 
"""

""" 
What we will do?
1.) print() function 
2.) Comments  
3.) Variable Assignment 
    - Assignment Operator  
    - Augmented Assignment  
    - Multiple Assignment  
    - Multuple Assignment   
4.) Identifiers  
5.) Module Structure  
6.) Intro to Memory Management In Python
"""


# ================== Using print() =======================
print("CS004 is a good course! I am really enjoying this course")

# adding two numbers ( example of a comment )
print(2 + 3)

# Multiple statements on the same line
print("CS001 is Great! ")
print(2 + 3) 

print("Hi Ayush");print("Hi You!")


# Assignment Operator
anInt = 25
anString = 'Cart'
anotherString = "Cart" + "Cape"  
print(anotherString)
anFloat = 2.5 * (1.5 * 6)

"""
Important Note : Be aware now that assignment does not explicitly assign a value to a variable,
although it may appear that way from your experience with other programming
languages. In Python, objects are referenced, so on assignment, a reference (not a
value) to an object is what is being assigned, whether the object was just created or
was a pre-existing object.
"""

# x = 1
# y = (x = x + 1)

# ======================= Variable Assignment =========================
'''Variables:- 

A variable name must start with a letter or the underscore character.
A variable name cannot start with a number.
A variable name can only contain alpha-numeric characters and underscores 
Variable names are case-sensitive 

'''
# Augmented Assignment
x = 1
x += 1

print(x)

y = 1
y += 1
print(y)

# Multiple Assignment

a = b = c = 1
print(a)
print(b)
print(c)

# Multuple Assignment

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

(a, b, c) = (1, 2, 3)

x, y = 1, 2
x, y = y, x

# ========================== Identifiers ====================================
""" 
Identifiers are the set of valid strings that are allowed as names in a computer
language. 

Some Idenitifiers are reserved words in python which is built for some kind of use case and In python  
We also have built-ins, these are also indentifiers, however we can use it because it is not reserved words,  
but it is not recommended to use. Examples listed below. 

What are some valid Identifiers? 
1.) First character must be a letter or underscore ( _ ) 
2.) Any additional characters can be alphanumeric or underscore 
3.) Case-sensitive 

Trick for checking whether the identifier is valid identifier or not? 
"""

print("arr".isidentifier())
# ===============================================================================

# ========================== Module Structure ====================================
"""
(1) module documentation
(2) module imports
(3) variable declarations
(4) class declarations
(5) function declarations
(6) "main" body
"""

# This is a test documentatio
import sys
import os

debug = True


class FooClass(object):
    pass


def add(a, b):
    c = a + b
    return c


if __name__ == "__main__":
    add()
# ==================================================================================

'''Assignments to work on:-  
1. Take a look at escape sequences in python and write all the escape sequences with examples. 
2.) take a look at print() function in the docs and figure out what more you can do with it. 
3.) Do bit of study of if __name__ == "__main__" 

''' 

# ===================================================================================
''' Notes about Comments:- Comments are the part of code which is very important part, comments are used to provide usual information about the code you have written. 
    There are two types of comments:- 
        - # ( In line comment ) 
        - """ """ ( Multi line comment)'''
