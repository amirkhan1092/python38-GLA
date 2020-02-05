# initialization
t = ()
t = tuple()

print(t, type(t))

# init tuple with single integer
t = (10,)
t = 10,

# tuple operation(access the elements)
# 1 indexing
t = (2, 43, 'hello', [2, 43])
d = t[-1]
print(d, type(d))

# slicing
t = (2, 43, 'hello', [2, 43])
d = t[-1:10]
print(d, type(d))
# output ([2, 43],) <class 'tuple'>

# item assignment
t = (2, 43, 'hello', [2, 43])
t[0] = 'hello'
print(t)
# output error TypeError: 'tuple' object does not support item assignment

# deletion
t = (2, 43, 'hello', [2, 43])
del t[0]
print(t)


# list in tuple
t = (2, 43, 'hello', [2, 43])
t[-1].append('Hi')
t[-1].clear()
print(t)


# using typecase
a1 = list(range(1, 1001))

# append
a2 = []
for i in range(1, 1001):
    a2.append(i)

# list comprehension
a3 = [i for i in range(1, 1001)]

# concat
a4 = []
for i in range(1, 1001):
    a4 += [i]






