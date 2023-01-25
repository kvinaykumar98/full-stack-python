Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> c=a+b
>>> print(c)
30
>>> a="mahesh"
>>> b= "reddy"
>>> a+b
'maheshreddy'
>>> a-b
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> a=20
>>> c=30
>>> a-c
-10
>>> d=2
>>> e=6
>>> d*e
12
>>> f=30
>>> g=10
>>> f/g
3.0
>>> x=20
>>> y=2
>>> x%y
0
>>> f%g
0
>>> s=23
>>> k=3
>>> s%k
2
>>> j=45
>>> l=9
>>> j//l
5
>>> s//k
7
>>> j/l
5.0
>>> t=5
>>> o=4
>>> t**o
625
>>> 2**3
8
>>> #comparison operator
>>> # compare two values
>>> 3>4
False
>>> # comparision operators returns boolean
>>> 6>7
False
>>> 8>6
True
>>> 34<3
False
>>> 45<46
True
>>> a=4
>>> b=4
>>> a>=b
True
>>> s=8
>>> f=6
>>> s>=f
True
>>> f>=s
False
>>> f<=s
True
>>> s<=f
False
>>> a=6
>>> b=6
>>> a==b
True
>>> d=7
>>> f=9
>>> d==f
False
>>> d!=f
True
>>> a!=b
False
>>> a=9
>>> a
9
>>> a=+b
>>> a=+1
>>> 
>>> 
>>> a=3
>>> a=+1
>>> b=a+=1
SyntaxError: invalid syntax
>>> a=3
>>> a=a+1
>>> a
4
>>> a=5
>>> a+=2
>>> a
7
>>> d=5
>>> d=+3
>>> d
3
>>> d*=3
>>> d
9
>>> d/=2
>>> d
4.5
>>> # logical operators
>>> # and,or,not
>>> a=20
>>> b=30
>>> c=40
>>> d=50
>>> a<b and c<d
True
>>> a<b and b<c and c>d
False
>>> a>b or b<c
True
>>> a<not b
SyntaxError: invalid syntax
>>> not a<b
False
>>> not a>b
True
>>> a=[1,2,3,4]
>>> b=5
>>> b in a
False
>>> b not in a
True
>>> a="vinay"
>>> b="kumar"
>>> a is b
False
>>> a="vinay"
>>> b="vinay"
>>> a is b
True
>>> a is not b
False
>>> ~a
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    ~a
TypeError: bad operand type for unary ~: 'str'
>>> ~6
-7
>>> 