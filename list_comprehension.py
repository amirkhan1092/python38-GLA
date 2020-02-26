def add(a):
    if a % 2 == 0:
        return a - 2
    else:
        return a-1

lst = [1, 2, 4, 7, 9, 34, 23]
out = [add(i) for i in lst if i]
print(out)
out = map(add, lst)

lst = [1,2,3,65,45]
out = [i**2 for i in lst if i%2==0]
print(out)

h = [(), '', 'hello', [33], (), '3']

lst = [i for i in h if i]







a = [1, 32, 5, 7, 54, 76, 22]



b = [1.8*i+32 for i in a]
print(b)

lt = []

lst = ['34', '21', '4', '76']
b = [int(i) for i in lst]
bm = map(int, lst)
print(b)
print(bm)

lst = ['34', '21', '4', '76', '43']
bm = list(map(int, lst))

k = next(bm)
for i in bm:
    u = list(bm)
    print(i)


1,3,9,12,15,20,28,32,33,36,38,48,50,53,54




k = ['33.0', '34', '12']
gen = map(eval, k)

first = list(gen)

for i in gen:
    print(i)
second = next(gen)


k = ['33.0', '34', '12']
gen = map(eval, k)

y = a, b, c = gen
print(y)

def apnafun(k):
    return k+2

l = [2, 45, 6]
k = list(map(apnafun, l))





b = ['ravi kumar', 'chandan thakur', 'mohan rajput', 'abhay kumar']
lst = [i.upper() for i in b if i.split()[-1] == 'kumar']
print(lst)
print(b)


k = [1, 3, 6, 54]
pt = []
p = [pt.append(i) for i in k]
print(p)


k = ['22', '3', '4', '65']
lst = [int(i) for i in k]



a = [343]
print(a)
# using range only
a1 = list(range(1, 1001))

# append
a2 = []
for i in range(1, 1001):
    a2.append(i)

# concat
a3 = []
for i in range(1, 1001):
    a3 += [i]

# list comprehension
a4 = [i for i in range(1, 1001)]
print(a4)


# using typecasting
a1 = range(1,1001)
print(a1)
# using append
a2 = []
for i in range(1, 1001):
    a2.append(i)

# list comprehension
a3 = [i for i in range(1, 1001)]

# concat
a4 = []
for i in range(1, 1001):
    a4 += [i]




# print(b)

# b = []
# for i in a:
#     b.append(i+2)
# print(a)
# print(b)

# b = [int(i) for i in a]
# print(a)
# print(b)


a = ['43', '3', '21']
km = map(int, a)

for i in km:
    print(i)
    o = list(km)

# traverse two list simultaneously
# 1list comprehension
L1 = [2, 4, 5, 8]
L2 = [3, 6, 2, 1]
L = [[L1[i], L2[i]] for i in range(len(L1))]

for i, j in L:
    print('elements from list 1', i)
    print('elements from list 2', j)

# using append
L1 = [2, 4, 5, 8]
L2 = [3, 6, 2, 1]
L = []
for i in range(len(L1)):L.append([L1[i], L2[i]])
for i, j in L:
    print('elements from list 1', i)
    print('elements from list 2', j)
