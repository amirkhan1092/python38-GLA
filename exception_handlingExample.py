'''

Error
1. Syntax Error : before Execution
2. Exceptions: After Execution or run time error


'''

# NameError
a = 10
b = 20
if a == b:
    c = 100

print(c ** 3)

# ValueError
h = int('sbaga')
print(h)

# TypeError
s = {2, 4, 6, 432}
h = s[1:33]
print(h)

# ZeroDivisionError
h = 12 / 0
print(h)


# Memory Error
def Zyx(*tt):
    pass


Zyx(*range(1000000000))


# RecursionError

def Xyz(r):
    Xyz(r + 100)


Xyz(100)


# UnboundLocalError
def xyz():
    print(x)
    x = 30


x = 10
xyz()

# AttributeError
s = None
s.remove('l')
print(s)

# EOFError
h = input('enter the somethings')  # CNTL+D
print(h, len(h))

f = open('shuriti.dat')

# StopIteration
h = iter([2, 5, 7])
next(h)
next(h)
next(h)
next(h)  # Stopeiteration

##ModuleNotFoundError
import satyam

# syntax Error
k = eval('2hghgh')
print(k, type(k))

# UnicodeEncodeError
h = 'hello⟚'
k = h.encode('ascii')
print(k)

exceptions - Handling

try-except format 1

'''
try:
    statements
except:
    statements 

'''

# example 1

try:
    k = int(input('enter the value '))
    print(k, type(k))

except ValueError:
    print('invalid integer ')


except (EOFError, KeyboardInterrupt):
    print('forcely stop')

except:
    print('Unknown Error ')

# example2

lst = [2, 3, 4, 'hello', 0, 2, 1, None]
out = []
try:
    for i in lst:
        out.append(1 / i)
    print(out)

except TypeError as t:
    print('Type error occured ', t)


except ZeroDivisionError as t:
    print('Wrong integer value ', t)

# example3
lst = [2, 3, 4, 'hello', 0, 2, 1, None]
out = []

try:
    for i in lst:
        try:
            out.append(1 / i)
        except TypeError:
            print('error with ', i)

    print(out)

except:
    print('not iterable ')

try-except- else format 2

'''
try:
    statements
except:
    statements
else:
    statements

'''

# example4
lst = [2, 3, 4, 2, 1]
out = []
try:
    for i in lst:
        out.append(1 / i)
    print(out)

except TypeError:
    print('Type error occured ')


except ZeroDivisionError:
    print('Wrong integer value ')


else:
    print('succesfully operation done ')

try-finally format 3

'''
try:
    pass
finally:
    pass

'''
print('program start ')
try:
    k = eval('[2, 3, 3 2]')
    print(k)
finally:
    print('good bye ')

try-except-finally

'''
try:
    pass
except:
    pass
finally:
    pass

'''
print('program start ')
try:

    k = eval('[2, 3, 3, 2]')

    print(k)

except NameError:
    print('error occured ')

finally:

    print('good bye ')

try-except- else -finally

print('program start ')
try:

    k = eval('[2, 3, 3, 2]')

    print(k)

except:
    print('error occured ')
else:
    print('operation done without fail ')

finally:

    print('good bye ')

assert True / False, 'message'

a = 170

assert a <= 150, 'High Temperature'

print('Temp', a)

raise TypeError
23 + [32]



