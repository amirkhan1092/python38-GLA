# example 1
import time


def countdown(x):  # x = 4
    if x == 0:
        pass
    else:
        print(x)
        countdown(x - 1)


v1 = time.time()
countdown(1000)
v2 = time.time()
print(v2 - v1)
print('Happy Recursion Day')
out1 = 0.014958620071411133


# countdown using iteration
def countdown(x):  # x = 4
    for i in range(x, 0, -1):
        print(i)


v1 = time.time()
countdown(1000)
v2 = time.time()
print(v2 - v1)
out2 = 0.011011362075805664
# time comparision
print(out1 - out2)


# example 1: countdown
def countdown(x):  # x = 5
    if x == 0:
        return 'stop'
    print(x)
    countdown(x - 1)


countdown(5)
print('happy recursion day')


# example 2: factorial
def fact(x):
    if x == 0:  # Base case
        return 1
    return x * fact(x - 1)


# p = 1
# x = 5
# p = 5*4*3*2*1*1
num = int(input('enter the number '))
out = fact(num)  # 5
print('factorial of given value', out)


# example 3: GCD or HCF
def gcd(x1, x2):
    # logic here with recursion
    if x1 > x2:
        return gcd(x1 - x2, x2)
    elif x2 > x1:
        return gcd(x1, x2 - x1)
    else:
        return x1


print(gcd(10, 12))


# example 3
# GCD
def gcd(x, y):
    # logic here
    if x > y:
        return gcd(x - y, y)
    elif x < y:
        return gcd(x, y - x)
    else:
        return x


print(gcd(10, 12))


# example4 ....min square in rectangle at given sides (simple format only sides is considering )
def min_sqr(r, w, c=0):
    if r > w:
        c += 1
        return min_sqr(r - w, w, c)
    elif r < w:
        c += 1
        return min_sqr(w - r, r, c)
    else:
        return c + 1


out = min_sqr(5, 2)
print(out)



lst = (i for i in range(10))
next(lst)
# shallow copy
lst = [2, 2, 1, 66, 9]
out = lst.copy()
lst.clear()
print(out)  # [2, 2, 1, 66, 9]
print(lst)  # []

# deep copy
import copy

lst = [[2], 2, 1, 66, {9}]
out = copy.deepcopy(lst)
out[0].append(100)
print(out)  # [[2, 100], 2, 1, 66, {9}]
print(lst)  # [[2], 2, 1, 66, {9}]


def my_fun():
    print('this is my function')


b = 'hell'
h = f'result is {b}'
print(format(123, 'd'))


def my_fun():
    a = 100
    print('hello')
    my_fun()


a = 100
my_fun()


# example 1 : countdown
def countdown(x):  # x = 4
    if x == 0:
        return 'stop'
    print(x)
    countdown(x - 1)


countdown(2)
print('happy recursion day')


def squar_min(r, w, c=0):
    '''
    user define function that return integer of minimum sqr
    '''
    if r > w:
        c += 1
        return squar_min(r - w, w, c)
    elif w > r:
        c += 1
        return squar_min(w - r, r, c)
    else:
        return c + 1


out = squar_min.__doc__
print(out)


# example 3: GCD
def gcd(x1, x2):
    if x1 > x2:
        return gcd(x1 - x2, x2)
    elif x2 > x1:
        return gcd(x1, x2 - x1)
    else:
        return x1


print(gcd(45, 15))


# example 4: traverse string with recursion

def my_fun(x):  # x = 'ello world'
    if x == '':
        return 'stop'
    print(x[0])  # 'e'
    my_fun(x[1:])


st = 'hello world'
my_fun(st)


# example 5: reverse string with recursive function
def my_fun(x):  # x = 'ello world'
    if x == '':
        return ''
    return my_fun(x[1:]) + x[0]


# my_fun('hello world')
# my_fun('ello world') + 'h'
# my_fun('llo world') + 'e' + 'h'
# .
# .
# my_fun('')+'d'........ + 'e' + 'h'

st = 'hello world'
out = my_fun(st)
print(out)

# example 6:
