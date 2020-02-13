
'''
False Evaluate Quantity
0, None, '', [], (), {}, set(), False
'''

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














