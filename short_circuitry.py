
'''
False Evaluate Quantity
0, None, '', [], (), {}, set(), False
'''











# combine two list

l1 = [2, 6, 8, 2, 9, 76]
l2 = [4, 8, 1, 0]
# l = [(l1[i], l2[i]) for i in range(len(l1))]
cc = len(l1) if len(l1) < len(l2) else len(l2)
l = []
for i in range(cc):
    l.append((l1[i], l2[i]))

print(l)
print(l1)
print(l2)






lst = [(2, 4), (6, 8), (8, 1), (2, 0)]
l1 = []
l2 = []
for i,k in lst:
    l1.append(i)
    l2.append(k)
print(l1)
print(l2)
1,2,3,4,


a = 10
b = 30

if None:
    print('a is greater than b')
else:
    print('b is greater than a')

# (and) Series connection
h = None and 10/0
print(h)

h = not not not True and not 'badminton'
print(h)

# (or)
h = () or ''
print(h)

a = 10
b = 30
k = 100 if '' or 'rakesh' and  [] else 200 if '' or '' else not 0 or 1
h = 'a is greater than b' if a>b else 'b is greater than a'
print(h)


'''
A   B   OUT
0   0   0
1   0   1
'''





a = 1
b = 0


out_xor = a ^ b
out_and = a & b
out_or  = a | b
out_not = not a


f = f'{a}   {b}     {out_xor}'














