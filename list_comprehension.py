a = [1, 2, 3, 43, 4, 23, 12, 3, 2, 8, 6]
# b = []
# for i in a:
#     if i%2 == 0:
#         b.append(i)

b = [i for i in a if i % 2 == 0]

print(b)
print(a)

b = ['ravi kumar', 'chandan thakur', 'mohan rajput', 'abhay kumar']
lst = [i.replace('kumar','singh') for i in b if i.endswith('kumar')]
print(lst)
print(b)


k = [1, 3, 6, 54]
pt = []
p = [pt.append(i) for i in k]
print(p)


k = ['22', '3', '4', '65']
lst = [int(i) for i in k]



a, t = [2, 4]
print(a, type(a))




# print(b)

# b = []
# for i in a:
#     b.append(i+2)
# print(a)
# print(b)

# b = [int(i) for i in a]
# print(a)
# print(b)