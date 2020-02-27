ls=[]
a=int(input('enter the length of list'))
for i in range (0,a):
    j=int(input())
    ls.append(j)
k=[]
s = [0]
c = ls.count(0)
for i in ls:
    if i != 0:
        k.append(i)
k.extend(c*s)
print(k)


# missing number in a series
x = eval(input())
d=[]
for i in range(1,x[-1]+1):
    if i not in x:
        d.append(i)
print(d)


s=input()
s=s.lower()
a=0
for i in range(97,123):
    if chr(i) not in s:
        a=1
if(a==1):
    print('Not a pangram')
else:
    print('Its a pangram')



# range with 7 and # lst[]
a = []
for i in range(2000,30001):
    if i % 7 == 0 and i % 5 != 0:
        a.append(str(i))
print(",".join(a))


# Sec -A Q2
lst = input().split(",")
tpl = tuple(lst)
print(lst)
print(tpl)

# Sec-A Q3
from math import factorial
t=map(int,input().split())
lst = []
for i in t:
    lst.append(str(factorial(i)))
print(','.join(lst))

# Sec B Q1
c=50
h=30
lst = []
s=input()
ls=s.split(",")
for i in ls:
    q=(2*c*int(i)//h)**.5
    lst.append(str(q))
print(','.join(lst))


# paper2 Sec- C Q1
l1=input().split("-")

l1.sort()
p="-".join(l1)
print(p)

# paper2 Sec- C Q2
a=eval(input())
b=eval(input())
l = list()
for i in a: l.append(i)
for i in b:
    if i not in l:
        l.append(i)
t = tuple(l)
print(t)

# paper2 Sec-C Q3
l=eval(input())
l1=list()
for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        continue
    else:
        l1.append(i)
print(l1)



# paper2 Sec- C Q4
l1=eval(input())
l2=eval(input())
l=[]
if len(l1)> len(l2):
    m= len(l2)
else:
    m= len(l1)
for i in range(m):
    l.append((l1[i],l2[i]))
print(l)
for i,j in l:
    print("elements from l1:",i)
    print("elements from l2:",j)

for i,j in zip(l1,l2):
    print(i)
    print(j)



# paper1 sec-C Q1
a=eval(input())
for i in range(len(a)):
    if a[i]==0 :
        a.remove(a[i])
        a.append(0)
print(a)

# paper1 sec-C Q3
a=eval(input())
b=[]
for i in range(a[0],a[-1]+1):
    if i not in a :
        b.append(i)
print(b)

# paper1 sec-C Q4

st = input().upper()
f=0
for i in range(65,91 ):
    if (chr(i) not in st):
        f=1
        break
if(f==0):
    print("pangram")
else:
    print("Not pangram")



# intersection between two string

st1 = input()
st2 = input()
b=''
for i in st1:
    if i in st2 and i not in b:
        b += i
print(b)























