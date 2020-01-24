# initialize the list (empty list)
ls = []
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

