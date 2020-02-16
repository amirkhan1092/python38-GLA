'''
str.format() is one of the string formatting methods in Python3,
which allows multiple substitutions and value formatting.
This method lets us concatenate elements within a string through positional formatting.
'''



a = 10
b = 30
c = a + b
f = f'result is {c} of {a} {b}'
f = 'result is {} of {} {}'.format(c, a, b)
f = 'result is %d of %d %d' % (c, a, b)
print(f)

k = 'my name is and my record is {0:10d}'.format(2)
print(k)
