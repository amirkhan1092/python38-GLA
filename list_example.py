# initialize the list (empty list)
ls1 = []
ls = list()
print(ls, ls1)
# output []
# init a list with single integer value
ls = [10]
#  output [10]

st = range(10)
ls = list(st)
print(ls)
print(st)
# output hello
# output ['h', 'e', 'l', 'l', 'o']

# indexing
# get the element at given position
ls = [1, 3, 65, 76, ['hello',0]]
ls[0] = 'hello'  # item assignment
d = ls[0]
print(d, type(d))
# output 1
# slicing
# get the subsequence(sub list ) at given range
ls = [1, 3, 65, 76, 'hello']
d = ls[1000:300000000]
print(d, type(d))
# output [1, 3, 65, 76]
# changeable item update
ls = [2, 5, 4, 43, 4, 5, 54]
ls[0] = 'hello'  # item assignment
ls[1:4] = ['ravi', 34]
print(ls)
# output ['hello', 'p', 'y', 't', 'h', 'o', 'n', 4, 5, 54]

# method in a list
# append add element in list
ls1 = [10, 34]
ls1.append('hello')
ls1.extend(range(4))
print(ls1)


# extend ....append iterable values in a list individual
ls1 = [2, 4 , 5]
ls1.append(10)
ls1.extend('hello')
print(ls1, len(ls1))

# insert
ls = [2, 5, 6, 9]
ls.insert(-1,'hello')
ls[-1] = 'Hi'
print(ls)
# output [2, 5, 6, 'hello', 'Hi']


# remove the elements from list

# remove
ls = ['tanishq', 'ravi', 'variable', 'tanishq']
ls.remove(ls[1])
ls.remove(ls[1])
print(ls)
# output ['tanishq', 'tanishq']

# pop
ls = [3, 2, 31, 5, 6]
k = ls.pop()
k = ls.pop(0)
k = ls.pop(1)
k = ls.pop()
k = ls.pop()
print('item removed ',k)
print(ls)

# item deletion
h = [2, 'hello', 'Hi']
del h[0]  # item deletion
print(h)

# 8,15,19,'26',32,'34',35,36,62
# clear
ls = [2, 5, 75, 3]
ls.clear()  # empty list
print(ls)


# copy
ls = [2, 5, 75, 3]
d = ls[:]
d[-1] = 'hello'

print(d)
print(ls)

# sorting with number
ls = [2, 6, 43, 0, 23]
ls.sort(reverse=True)
print(ls)

# sorting with string ascii
ls = ['rAvi','akash','aNjali','Zebra','tarun']
ls.sort()
print(ls)
# ['akash', 'anjali', 'ravi', 'tarun', 'zebra']

# sorting with function
ls = ['ravi',['akash','aNjali'],'Zebra','Tarun']
ls.sort(key=len)
print(ls)
# [['akash', 'aNjali'], 'ravi', 'Zebra', 'Tarun']

# sorting with string max char in length
ls = ['ravi','akash','aNjali','Zebra','Tarun','aa','AA']
ls.sort(key=max)
print(ls)
# ['aNjali', 'Zebra', 'akash', 'Tarun', 'ravi']

# reverse
ls = [2, 'hello', 'Hi', 'Python', 23]
# ls = ls[::-1]
ls.reverse()
print(k)

# index
ls = [1, 2, 'hello', 'Hi', 'Python', 23, 2]

element = 2
k = 0
c = ls.count(element)
print('number of elements ', c)
for i in range(c):
    k = ls.index(element,k+1)
    print('position ', k)





ls.count(2)
print(k)  # output 5

# count
ls = [2, 'hello', 'Hi', 'Python', 23, 'Hi']
k = ls.count('Hi')
print(k)


# copy
ls = [2, 33, 'hello']
d = ls.copy()

print(id(ls))
print(id(d))





