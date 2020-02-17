
'''
False Evaluate Quantity
0, None, '', [], (), {}, set(), False
'''

# and
out = 'abc' and None
print(out, type(out))  # None class<NoneType>

# or
out = False or 'abc'
print(out, type(out))  # 'abc' class<str>


first = 1
second = True

out = 'first' if first == second else 'first' and 'second'
nz = eval(out)
print(nz, type(nz))


true = 'false of y'
false = true
y = false

print(eval(eval('true')[-1]))






# combine two list(merge two list items )
l1 = [2, 6, 8, 2]
l2 = [4, 8, 1, 0]

# out = [(2, 4), (6, 8), (8, 1), (2, 0)]

out = zip(l1, l2)

# for i in range(len(l1)):
#     out.append((l1[i], l2[i]))
#
# print(out)



out = [(2, 4), (6, 8), (8, 1), (2, 0)]


l1= [out[i][0] for i in range(len(out))]
l2 = [out[j][1] for j in range(len(out))]
print(l1,l2)
new_l2 = []
new_l1 = []
for i,j in out:
    new_l1.append(i)
    new_l2.append(j)
print(new_l1)
print(new_l2)





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














