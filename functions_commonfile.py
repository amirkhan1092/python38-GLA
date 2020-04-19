# function
def Sum(n1, n2):
    return n1 + n2

num1 = 12
num2 = 21
res = Sum(num1, num2)
print(res)

# function2
def print_sum(n1, n2):
    print('Sum of two numbers is ', n1 + n2)

num1 = 12
num2 = 21
print_sum(num1, num2)


def type_sum(v1, v2):
    type1 = [int, list, str, tuple]
    type2 = [dict, set]
    if type(v1) in type1 and type(v2) in type1:
        res = v1 + v2
        return f'value is ordered or integer number, sum is {res}'
    else:
        v1.update(v2)
        return f'values are unordered merge file {v1}'
value1 = eval(input('enter the first value '))
value2 = eval(input('enter the second value '))
print(type_sum(value1, value2))



# positional
def add( y, k = 0):
    print('first argv ', k)
    print('second argv ', y)

add(5,)

# optional values
h, k, *u = (6, 9, 78, 7)

#
# def type_sum(a, b):
#     if type(a) == dict or type(a) == set:
#         a.update(b)
#         return f'values are unordered and merge value is {a}'
#     else:
#         re = a + b
#         return f'values are ordered and sum/merge is {re}'
#
# v1 = eval(input('enter the first value '))
# v2 = eval(input('enter the second value '))
# c = type_sum(v1, v2)



# arguments in Python Function
# default arguments
def add(a, b=0): # right
    return a + b
k = add(8)
print(k)

def add(a=0, b): # error
    return a + b
k = add(7, 8)
print(k)

# built-in Example
print(int('67', 8))  # 8 is default argv



# positional arguments
def add(a, b):
        print('at first position ', a)
        print('second position ', b)

k = add( 30, 'rishabh')
print(k)




# optional positional arguments
def add(a, b, *t):
    print('at first position ', a)
    print('second position ', b)
    print('optional argv', t)

k = add('rishabh', 80)
print(k)



def optional_sum(*opt, a=0, b=0):
    return sum(opt)

h = optional_sum(7, 8, 9, 5, 4, 4, a = 7, b= 78)
print(h)


print(8, 'hello', 9.0, 89, sep='*')



def disp(*t, sap=' ', nnd='\n' ):  # t = ('hello', 8, 60, 8.0)
    k = sap.join(map(str, t))
    print(k,end='')
    print(nnd, end='')

disp("hello", 8, 60, 8.0, nnd='\n')
disp("Next command ")


# default arguments
# positional Argv
# optional Positional Argv

# keyword arguments  : arguments with names
def add(a, b):
    return a**2, b**3

sqr, cube = add( b=2, a=3)
print('square', sqr)
print('Cube', cube)


# Keyword arguments
def info_show(name, rolln, section, address):
    re = '''
            Name : {}
            Roll Number : {}
            Section : {}
            Address : {}
    '''. format(name, rolln, section, address)
    return re

k = info_show( section='3', address='GLA University', rolln=30, name='ravi')
print(k)

# optional keyword arguments
def info_show(**dt ):
    # {'Section': '3', 'Address': 'GLA University', 'NaMe': 'ravi', 'rolln': 30, 'cpi': 9.0}

    for i in dt.copy():
        dt[i.lower()] = dt.pop(i)
    re = '''
            Name : {}
            Roll Number : {}
            Section : {}
            Address : {}
    '''. format(dt.get('name'), dt.get('rolln'), dt.get('section'), dt.get('address'))
    return re

k = info_show( Address='GLA University', NaMe='ravi', Rolln=30, CPI=9.0)
print(k)

# global and local : define terms only based on output
def my_fun():
    var = 10  # local variable
    print(var)  # local print 10

var = 20  # global variable
my_fun()
print(var)  # global value 20

# global keyword : allow the permission to use the global variable
def my_fun():
    global var   # permission to write and read in global variable
    var = 8    # change in global value with variable var
    print(var)  # global variable 8


var = 10 # global variable
my_fun()
print(var) # global value 8



# unbound error
def my_fun():
    print(var)  # var as global read only
    var = 0 # new variable a local

    var = var + 20  #
var = 20
my_fun()
print(var)



# local variable
# example 1
def my_fun():
    var = 10


my_fun()
print(var)  # name error 'var'


# example 2
def my_fun():
    global var  # permission to use global scope variable
    var = 10
my_fun()
print(var)  # output 10







# scope of variable
'''
local : variable inside function
global : keyword that give to access the global 
nonlocal : keyword that give to access the nonlocal
'''


def my_fun():
    def inner():
        k = 78
    def inner_non():
        nonlocal k
        k = 60
    def inner_global():
        global k
        k = 90
    k = 0
    inner()
    print(k)  # 0
    inner_non()
    print(k) # 60
    inner_global()
    print(k)  # 60

k = 1  # global scope
my_fun()
print(k)  # 90



# scope of variable

# global scope

def my_function():
    a = 90  # local variable
    print(a)  # local value

a = 0  # global variable
my_function()
print(a) # global values



# global keyword :
def my_fun():
    global a  # allow the permission to use the global scope
    a = 90

a = 0
my_fun()
print(a)  # output : 90



# local and global
def my_fun():
    global x
    x = 'HI'
    y = 'HELLO'

x = 'hi'
y = 'hello'
my_fun()
print(x)  # 'HI'
print(y) # 'hello'

# non local
def my_fun():
    def fun_1():
        def kmp():
            global d
            d = 1100
        d = 1
        kmp()
        print(d)  # 1
    def fun_2():
        nonlocal d  # allow the permission for non local scope
        d = 2
    def fun_3():
        global d  # allow the permission for global scope
        d = 3
    d = 0
    fun_1()
    print(d)  # 0
    fun_2()
    print(d) # 2
    fun_3()
    print(d) # 2

d = 100  # global variable
my_fun()
print(d)  # 3



# lambda function
f_to_h = lambda x : (x-32)/1.8
fah = int(input('enter the fah value '))
k = f_to_h(fah)
print('cel value ', k)


k = [7, 9, 4, 34, 56]

re = map(lambda x : (x-32)/1.8, k)






def my_fun():
    def fun_1():
        def kmp():
            global h
            h = 565
        h = 1
        kmp()
        print(h)  # 1
    def fun_2():
        nonlocal h # allow the permission to use the non local scope
        h = 2
    def fun_3():
        global h # allow the permission to use the global scope
        h = 3
    h = 10  # local (for nested function h is non-local)
    fun_1()
    print(h)  # 10
    fun_2()
    print(h)  # 2
    fun_3()
    print(h)  # 2

h = 0  # global variable
my_fun()
print(h)  # global value  output: 3




# variable scope in Python
def my_fun():
    def fun_1():
        def kmp():
            nonlocal k
            k = 800
        k = 1
        kmp()
        print(k) # 1
    def fun_2():
        nonlocal k  # allow the permission to use nonlocal scope
        k = 2
    def fun_3():
        nonlocal k  #
        k = 3
    k = 20  # local variable (nonlocal for nested function)
    fun_1()
    print(k)  # 20
    fun_2()
    print(k)  # 2
    fun_3()
    print(k)  # 3

k = 0  # global variable
my_fun()
print(k)  # 800
# \

# consecutive integer groups : competitive coding
# for _ in range(int(input())):
#     p = int(input())
#     lst = []
#     ls = list(map(int, input().strip().split()))
#     tmpl = []
#
#
#     for i in range(len(ls)-1):
#         if ls[i+1] - ls[i] == 1:
#             tmpl.append(ls[i])
#             if i == len(ls)-2:
#                 tmpl.append(ls[i+1])
#                 lst.append(tmpl)
#
#         else:
#             tmpl.append(ls[i])
#             lst.append(tmpl)
#             tmpl = []
#     print(lst)
#     print(len(list(filter(lambda x:len(x)>1, lst))))




# lambda function

#
ls = [2, 45, 23, 4, 12]
out = list(map(lambda a: 'special number' if a > 20 else 'normal number ', ls))
print(out)



k = [('animesh', 21), ('tanishq', 41), ('vasundhara', 40), ('ram', 26)]
# [('tanishq', 41), ('vasundhara', 40), ('ram', 26), ('animesh', 21)]
k.sort(key=lambda x:x[1])
print(k)



# def prime(n):
#     count = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             count += 1
#
#     if count == 2:
#         return 'prime number '
#     else:
#         return 'not Prime number'


# lambda function
def Add(a, b):  # function with def
    return a + b

Add = lambda a, b : a + b  # function with lambda keyword
k = Add(2, 6)
print(k)


# cel to fah
cel_to_fah = lambda x:(x-32)/1.8
c = int(input())
fh = cel_to_fah(c)
print(fh)



k = ['23', '34', '3', '0']
lst = list(map(lambda y:'0'+y, k))
print(lst)



k = [('3', '0', '1') , ('7', '5', '44')]
lst = list(map(lambda i:''.join(i), k))
print(lst)


k = '*'.join('hello')
print(k)



# lambda functions
# example 1
add = lambda a, b: a + b
k = add(2, 6)
print(k)


# example 2
cel2fah = lambda x : x*1.8 + 32
cel = int(input())
fah = cel2fah(cel)
print(fah)



# example 3 : convert all values(cel) into fah

lst = [45, -40, 48, 20, -100]
out = list(map(lambda c: c*18 + 32, lst))
print(out)


# example 4 : sort list with surname Alphabetically
lst = ['rajan tyagi', 'rahul sharma', 'xyz gupta', 'abhinav pandit']
lst.sort(key=lambda h:h.split()[1])
print(lst)
# sorting on length
lst = ['rajan tyagi', 'rahul sharma', 'xyz gupta', 'abhinav pandit']
lst.sort(key=lambda h:len(h.split()[1]))
print(lst)



# filter() the odd numbers values
ls = [2, 5, 7, 98, 2, 1, 9, 23]
odd = list(filter(lambda x: x % 2, ls))
print(odd)


# min()/max()
# example 1
ls = [2, 54, 7, 43, 987]
out1 = min(ls)
out2 = max(ls)
print(out1)  # 2
print(out2)  # 987

# example 2
ls = ['hello', 'hi', 'ravi', 'class', 'abc xyz ghd']
out1 = min(ls, key=len)
out2 = max(ls, key=len)
print(out1)  # 'hi'
print(out2)  # 'abc xyz ghd'



# map
# filter
# min()/max()


# map
k = [5, 89, 4, 45]
out = list(map(lambda x: x+2, k))
print(out)

# filter : filter odd values

k = [7, 4, 3, 2, 90, 45]
odd = list(filter(lambda x: x % 2, k))
print(odd)


# lambda with sort
# odd positions
# example 1
k = [7, 4, 3, 2, 90, 45, 8, 6, 5, 2, 88, 89]
k.sort(key=lambda x:x%2)
print(k)

# example 2 sorting with surname alphabetically
k = ['ruchi gupta', 'rahul sharma', 'abhinav pandey', 'rishabh garg', 'saransh pathak']
k.sort(key=lambda x:x.split()[-1])
print(k)

# example 2 sorting ascii-weight
k = ['ruchi gupta', 'rahul sharma', 'abhinav pandey', 'rishabh garg', 'saransh pathak']
k.sort(key=lambda x:sum(map(ord, x)))
print(k)

# map()
# filter()
# sort()/sorted()
# min()
# max()


h = [6, 18, 3, 7, 2, 5, 60, 23, 50]
out = list(filter(lambda t: t>=10, h))
print(out)


h = [6, 18, 3, 7, 2, 5, 60, 23, 50]
out = list(map(float, h))
print(out)

# argv types in function
# pass by value and pass reference
# immutable vs mutable


def my_fun(h): # h = x
    h.add(100)

# mutable type
vr = {6, 8}
x = vr.copy()
k = my_fun(x)
print(vr)


# # immutable type
# vr = 'hello'
# k = my_fun(vr)
# print(vr)



# min()/max()
# sort()/sorted()
# map
# filter
l = ['hello', 'Hzzz', 'Abhinav', 'rajan']
out = min(l, key=lambda t: sum(list(map(ord, t))))


from functools import reduce
k = [1, 3, 4, 6]
out = reduce(lambda x1, x2:x1*x2, k)
print(out)


# data types of arguments
# pass by value and pass by reference
# mutable vs immutable

def my_fun(x):  # x = v
    x.clear()


# mutable
v = [2, 4, 7]
my_fun(v.copy())
print(v)


# immutable
v = 'hello'
my_fun(v)
print(v)


def sorted_or_not(k):
    # logic here
    # x = k.copy()
    # x.sort()
    # return x == k
    return k == sorted(k)

lst = [2, 5, 8, 0, 2, 4, 1]
out = sorted_or_not(lst)
print(out)





# map()
# filter()
# sort()/sorted()
# min()
# max()
# reduce() need to import module functools

sorted()  # built-in
l.sort()  # method of list object

h = (2, 34, 2, 1, 8)
h.sort(reverse=True)
print(h)
out = sorted(h, reverse=True )



h = [2, 34, 2, 1, 8, 4, 3, 5]
out = sorted(h, key=lambda x:x%2)
print(out)




# min()/max()
k = [2, 4, 4, 32, 9]
o1 = min(k) # 2
o2 = max(k) # 32


# min/max
# example 1 : default sort
k = ['hello', 'abhinav', 'ravi', 'venky']
o1 = min(k)  # 'abhinav'
o2 = max(k)  # 'venky'

# example 2 # based on length
k = ['hello', 'abhinav', 'ravi', 'venky']
o1 = min(k, key=len)  # 'ravi'
o2 = max(k, key=len)  # 'abhinav'

# example 3 # ascii-weight
k = ['hellozz', 'abhinav', 'ravi', 'venky']
o1 = min(k,key=lambda x:sum(map(ord, x)))
o2 = max(k, key=lambda x:sum(map(ord, x)))
print(o1)  # 'ravi'
print(o2) # 'hellozz'

import functools
k = [1, 3, 5, 6, 2]
out = functools.reduce(lambda x1, x2: x1*3/x2, k)
print(out)  # 180

# data types of argument
# pass by value and pass by reference
# mutable vs immutable




#  lambda function/ lambda expression

# def my_fun(a, b):
#     return a**2+b**2

my_fun = lambda a, b:a**2+b**2
out = my_fun(2, 4)
print(out)  # 20


# map()
# filter()
# sort()/sorted()
# min()/max()
# reduce()

# map()
# example 1
k = [1, 3, 4, 2, 4, 8, 23, 20]
out = list(map(float, k))
print(out)
# [1, 3, 4, 2, 4, 8, 23, 20]
# [1.0, 3.0, 4.0, 2.0, 4.0, 8.0, 23.0, 20.0]

# example 2 # square of list elements using map and lambda
k = [1, 3, 4, 2, 4, 8, 23, 20]
out = list(map(lambda x:x**2, k))
print(out) #[1, 9, 16, 4, 16, 64, 529, 400]

# example 3 square of selected items
k = [1, 3, 4, 2, 4, 8, 23, 20]
out = list(map(lambda x:x if x % 2 == 0 else x**2, k))
print(out)  # [1, 9, 4, 2, 4, 8, 529, 20]


# filter
# example 1 # filter the odd value
def my_fun(x):
    if x % 2 == 0:
        return False
    else:
        re
k = [1, 3, 4, 2, 4, 8, 23, 20]
out = filter(my_fun, k)




# call by value: valid for Python
# call by reference

def my_fun(x): # x = v
    x.clear()

# mutable
v = [3, 4, 7]
my_fun(v)
print(v)

# immutable
v = 'hello'
my_fun(v)
print(v)  # 'hello'





def my_fun(t, ls=[]):  # ls = [100, 101, 111]
    for i in range(t):
        ls.append(i*i)
    return ls

print(my_fun(2)) # [0, 1]
print(my_fun(3, [100, 101, 111]))  # [100, 101, 111, 0, 1, 4]
print(my_fun(4)) # [0, 1, 0, 1, 4, 9]



# filter: filter odd values
d = [22, 4, 7, 1, 7, 8, 34]
k = list(filter(lambda x: x%2==0, d))
print(k)



# sort()
# example 1 simple sorting default
d = [22, 4, 7, 1, 7, 8, 34]
d.sort()
print(d)

# Example 2 with string
d = ['hello', 'anant', 'ravi', 'xyz']
d.sort()
print(d)  # ['anant'...]

# example 3 custom sorting
d = ['hello world', 'anant', 'ravi', 'xyz', 'Hi']
d.sort(key=len)
print(d)  # ['Hi', 'xyz', 'ravi', 'anant', 'hello world']


# example 4 ASCII weight
d = ['hello world', 'anant', 'ravi', 'xyz', 'Hi']
d.sort(key= lambda x:sum(map(ord, x)))
print(d)

# Data type of arguments
# call by value and call by reference : call by value is only valid in python
# mutable vs immutable
def my_fun(x): # x = v
    x.clear()

# mutable
v = [3, 4, 6]
my_fun(v)
print(v)  # []


# immutable
v = 'hello'
my_fun(v)
print(v)



from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

print(fib(6))

def apna(x1, x2):
    print(x1,'-:-', x2)


print(reduce(apna, [12, 4,1], 5))








