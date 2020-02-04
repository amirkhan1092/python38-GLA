# string
# initialization
a = 'hello'
print(len(a), type(a))

# element indexing
d = a[-6]
print(d, type(d))

# slicing : substring from string data

h = 'hello world'
d = h[-3::1]
print(d, type(d))


# type cast with string
# number
k = int('1010',8)
print(k, type(k))

k = float('2.4')
print(k, type(k))


# list
st = '[2, 43, 4]'
lst = list(st)
print(lst, type(lst))

lst2 = eval(st)
print(lst2, type(lst2))

hello = 10

k = eval('hello')
print(k, type(k))

# list from from user
lst = eval(input('enter the list '))
print(lst)


# method

# split
k = '213 43 443 23 23  212'
out = k.split()

print(out, type(out))



