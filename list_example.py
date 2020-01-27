# initialize the list (empty list)
ls1 = []

ls = list()
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
ls = [1, 3, 65, 76, 'hello']
d = ls[0]
print(d)
# output 1
# slicing
# get the subsequence(sub list ) at given range
ls = [1, 3, 65, 76, 'hello']
d = ls[-3:-1:-2]
print(d)
# output [1, 3, 65, 76]
# changeable
ls = [2, 5, 4, 43]
ls[0] = 'hello'
print(ls)

# method in a list
# append add element in list
ls1 = []
ls1.append([2,4,5,7])
ls1.append((10,))
ls1.append(23)
# print(ls1, len(ls1))
# extend ....append iterable values in a list individual
ls1.extend([2, 4, 7, 6])
print(ls1, len(ls1))

# remove the elements from list
ls = [2, 4, 7, 8]
# item deletion
del ls[0]
print(ls)

# remove
ls = [2, 6, 87]
ls.remove(ls[0])
print(ls)

# pop
ls = [3, 6, 8]
k = ls.pop()
k = ls.pop(0)
k = ls.pop()
print('item removed ',k)
print(ls)









