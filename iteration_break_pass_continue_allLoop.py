
# Python Loop




1
# 1. for loop
'''
The for statement in Python differs a bit from what you may be used to in C or Pascal. 
Rather than always iterating over an arithmetic progression of numbers, 
or giving the user the ability to define both the iteration step and halting condition (as C), 

Python’s for statement iterates over the items of any sequence 
(a list or a string), in the order that they appear in the sequence. 
For example :

'''

for i in range(10):
    print('first',i*i)
    if i > 5:
        pass
    print('second', i+i)

else:
    print('loop complete ')







#The break statement, breaks out of the innermost enclosing for or while loop
# break just stop the iteration within the loop



#The continue statement, continues with the next iteration of the loop:

for i in range(10):
    print('single ',i)
    if i > 5:
        continue
    print('with expression', 2*i+2)

else:
    print('loop completed ')


# pass : pass just a keyword. it pass the instruction (do nothing). use to maintain the scope
def fun(r):
    pass

h = fun(34)

while 1:
    pass


for i in range(10):
    if i == 2:
        pass
    else:
        print(i**2)


def abcd(a, ll=[]):
    for i in range(a):
        ll.append(i*i)
from list_comprehension import l
print(l)




def apna_fun(t):
    for i in range(2, t):
        if t % i == 0:
            return 10
    else:
            return 0

L = [2, 4, 76, 23, 7, 23, 76, 3, 11, 17, 19]
L.sort(key=apna_fun)
print(L)

L = ['surabhi', 'akansha', 'neha', 'sneha']
L.sort(key=len)
print(L)




a = 1
while a:
    a = int(input('enter the number '))
    if a > 10:
        break
else:
    print('loop out')


s = input()
w, d = 0, 0
for i in s:
    if i == '\n' or i == '\t' or i == '\r' or i == ' ':
        w += 1
    elif '9' >= i >= '0':
        d +=1
print(w, d)

l = [2, 4, 6, 3, 6]
y = [0, 5, 7, 1, 90]

[[2, 0], [4, 5], [6, 7], [3, 1], [6, 90]]



# [22, 3.7, 'hello', 2+4j]
# h = eval(input())
hh = input().split()
print(hh)
h = list(map(eval, hh))
print(h)

if len(h) == 0:
    print('Empty')
for i in h:
    if type(i) not in [int, float]:
        print('No')
        break
else:
    print('Yes')



1
h=10
r=5
R=15
vol=3.14*(r**2)*h
t=int(input('enter the time in min'))
v=R*t
if vol==v:
    print('full')
elif vol<v:
    print('overflow')
elif vol>v:
    print('underflow')

s=input()
b=''
for i in s:
    if 'a' <= i <='z':
        b+=chr(ord(i)-32)
    elif 'A'<= i <= 'Z':
        b+=chr(ord(i)+32)
    else:
        b += i
print(b)