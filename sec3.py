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

# capitalize()
k = '2hello world'
out = k.capitalize()
print(out)

# upper
k = '2hello world'
out = k.upper()
print(out)
# output 2HELLO WORLD

# lower
k = '2Hello world'
out = k.lower()
print(out)
# output 2hello world





# center
k = 'hello6'
out = k.center(11, '*')
print(out)
# output hello*****

# rjust
k = 'hello'
out = k.rjust(10, '*')
print(out)


# rjust
k = 'hello'
out = k.ljust(10, '*')
print(out)


# zfill
k = '-12232'
out = k.zfill(10)
print(out)
# output -000012232


# encode
k = 'helloϪ'
out = k.encode('utf', errors='replace')
print(out, type(out))

out2 = out.decode('utf')
print(out2, type(out2))


# maketrans, translate

k = 'hello world'
intab = 'abcdef'
outab = '123456'
trans = str.maketrans(intab, outab)

out = k.translate(trans)
print(out)



# list
# list creation
a = []  # list format
a = list()  # using constructor
print(a)  # []

# init a list with single object
a1 = [10]
a2 = ['hello']
a3 = [[3,4]]


# accessing the elements
#     1. indexing : value at given position

k = [2, 43, 'hello', 1+3J]
d = k[-1]
print(d, type(d))  # (1+3j) <class 'complex'>

#       2. slicing: values at given range
k = [2, 43, 'hello', 1+3J]
d = k[10:1:-1]
print(d, type(d))


# other operation
# membership operator
ls = [2, 4, 5]
i = 3
out = i in ls
print(out)  # False
out = i not in ls
print(out)  # True

# concat
l1 = [2, 5]
l2 = [3]
l = l1 + l2

print(id(l))
l += [10, 11]
print(id(l))

print(l, type(l))  # [2, 5, 3, 8] <class 'list'>


# multiplication
ls = [2, 5]
out = ls*2
print(out)

# methods in list








