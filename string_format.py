'''
str.format() is one of the string formatting methods in Python3,
which allows multiple substitutions and value formatting.
This method lets us concatenate elements within a string through positional formatting.
'''

a = 10
b = 30
c = a + b
temp = 'result is %d of %d and %d'
f = temp % (c, a, b)
print(f)







# tag f format
a = 10
b = 30
c = a + b
temp = f"result is {c} of {a} and {b}"

print(temp)  # result is 40 of 10 and 30


f = f'result is {c} of {a} {b}'
print(f)  # result is 40 of 10 30



dh = 'result is {} of {} {}'
f = dh.format(c, a, b)
print(f)  # result is 40 of 10 30

f = 'result is %d of %d %d' % (c, a, b)
print(f)

k = 'my name is  and my record is {:10d}'. format(22223)
print(k)


