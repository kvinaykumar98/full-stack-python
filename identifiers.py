Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # identifiers
>>> # it is used to store the values or refer the values.
>>> # a name in python is knoen as variable or identifier or class name or function name
>>> # how to create variable
>>> a= 10
>>> a
10
>>> # here the 10 value is assined to 'a' variable
>>> # rules of identifier
>>> # Only Alphabets, digits, underscore symbol are only allowed to use.
    # Special symbols are not allowed.
    # Identifiers should not start with digit.
    # Identifiers are case sensitive.
    # We cannot use keywords as identifiers.
    
>>> a=30
>>> a
30
>>> a12=40
>>> a12
40
>>> _12=45
>>> _12
45
>>> _12
45
>>> 
>>> 
>>> _12
45
>>> _a12=567
>>> _a12
567
>>> 12=56
SyntaxError: cannot assign to literal
>>> @=34
SyntaxError: invalid syntax
>>> # variables are case sensitive
>>> abc=30
>>> abc
30
>>> ABC=40
>>> ABC
40
>>> Abc=50
>>> Abc
50
>>> id(abc)
2122388303056
>>> id(ABC)
2122388303376
>>> id(Abc)
2122388303696
>>> # keywords are reserved words
>>> # These are the reserved words to represent some meaning or funcionality
>>> # what are the keywords
>>> # how to import keywords
>>> import keywords
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 