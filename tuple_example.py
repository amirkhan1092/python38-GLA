# initialization Empty tuple
t = ()
t = tuple()  # constructor
print(t, type(t))  # () <class 'tuple'>

# init tuple with single object
t = (20,)
a = 20,
print(a, type(a))

t = ((2,),)
print(t, type(t))  # ((2,),) <class 'tuple'>

# tuple operation
# accessing the elements
#     1. indexing : element a position
t = (2, 43, 'hello', [2, 43])
d = t[1]
print(d, type(d))  # 43 <class 'int'>

#     2. slicing : elements at given range
t = (2, 43, 'hello', [2, 43])
d = t[11:1:-2]  # (43, 'hello')
print(d, type(d))  # (43, 'hello') <class 'tuple'>


# item assignment
t = (2, 43, 'hello', [2, 43])
t[-1] = 'hello'  # TypeError: 'tuple' object does not support item assignment
print(t)
# output error

# item deletion
t = (2, 43, 'hello', [2, 43])
del t[0]  # TypeError: 'tuple' object doesn't support item deletion
print(t)
# output error


# list in tuple
t = (2, 43, 'hello', [2, 43])
t[-1].append('Hi')  # list can add or remove the elements
print(t)
# without changing there id in namespace
t[-1].clear()
print(t)  # (2, 43, 'hello', [])

# tuple creation with multiple elements numbers
# using tuple constructor or typecast
a1 = tuple(range(1, 10))
print(a1, type(a1))  # (1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'tuple'>

# using concat
a2 = ()
for i in range(1, 10):
    a2 += (i,)  # two tuples can concat or append like string but change the id every time
print(a2, type(a2))  # (1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'tuple'>


# tuple generator (iterator)
a3 = (i for i in range(1, 10))
print(a3, type(a3))  # <generator object <genexpr> at 0x0E324F30> <class 'generator'>
# A generator is a special kind of iterator, which stores the instructions for
# how to generate each of its members, in order, along with its current state
# of iterations. It generates each member, one at a time, only as it is
# requested via iteration.

tp = tuple(a3)  # gen to tuple type
print(tp, type(tp))  # (1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'tuple'>


# tuple other operation

# membership
t = (2, 4, 6, 89, [1, 4])
item = 1
out = item in t
print(out)  # True
item = 100
out = item  in t
print(out)  # False

# multiplication with number
t = (2,5)
out = t*2
print(out, type(out)) # (2, 5, 2, 5) <class 'tuple'>

out = t*0
print(out, type(out))  # () <class 'tuple'>

# Addition (concat)

t1 = (2, 4)
t2 = (4, 8)
t = t1 + t2
print(t, type(t))  # (2, 4, 4, 8) <class 'tuple'>

# iteration with tuple (traverse)
t = (2, 54, 'hello')
for i in t:
    print(i)
# 2
# 54
# hello

# methods in tuple
'''
Only methods in tuple 
1. index 
2. count

both methods returns integer value

'''
# index : return match index of the element
t = ('a', 'h', 'Hi', 2, 65)
out = t.index(2)
print(out)  # 3

out = t.index('Hello')  # ValueError: tuple.index(x): x not in tuple
print(out) # error

# count : count the frequency of the elements within the tuple
t = ('a', 'h', 'Hi', 2, 65)
out = t.count(2)
print(out)  # 1

out = t.count('Hello')
print(out)  # 0

# colon
import copy
d = [2, 4, [7]]
t = copy.deepcopy(d)
t[-1].append(100)
print(t)
print(d)

u = [2, 4, [4]]
y = str(u)
t = eval(y)
p--rint(t, type(t))


h = range(1, 101)
even = []
odd = []
for i in h:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)

# print(d[-1] is t[-1])



# deepcopy using raw data

k = [2, 4, [3, 5]]
raw_data = str(k)
print(raw_data, type(raw_data))

lst = eval(raw_data)
lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(len(lst)):
    tt = list(lst[i])
    tt[-1] = 100
    tt = tuple(tt)
    lst[i] = tt
print(lst)

