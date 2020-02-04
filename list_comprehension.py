a = [1, 32, 5, 7, 54, 76, 22]
# b = []
# for i in a:
#     if i%2 == 0:
#         b.append(i)
b = [i for i in a if i % 2 == 0]
print(b)
print(a)


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




# print(b)

# b = []
# for i in a:
#     b.append(i+2)
# print(a)
# print(b)

# b = [int(i) for i in a]
# print(a)
# print(b)