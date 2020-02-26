ht = int(input('enter the height'))
pos = int(input('enter the position '))
k = 0
for i in range(1, ht+1):
    print(' '*(ht - i), end='')
    while k != 2*i-1:
        if k == 0 or k == 2*i-2:
            print('*', end='')
        elif i == pos:
            print('*', end='')
        else:
            print(' ', end='')
        k += 1
    k = 0
    print()

   # print('✪', end='')
   #      elif i == pos:
   #          print('❤', end='')



a = 'hello python class start at 10:00AM'
a=input()
d = 0
s = 0
for i in a:
    if i.isdigit():
        d+=1
    elif i == '\n' or i == '\t' or i == ' ':
        s+=1
print(d)
print(s)
s=input()
k = ''
for i in s:
    if i.isdigit():
        continue
    else:
        k = k+i
print(k)






