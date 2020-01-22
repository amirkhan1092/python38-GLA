h = 10
p = 0
for i in range(1, h+1):
       print(' '*(h-i),end = '')
       while p != 2*i-1:
           if p == 0 or p == 2*i-2 or i == h:
                print('*',end='')
           else:
                print(' ',end='')
           p += 1
       print()
       p = 0
