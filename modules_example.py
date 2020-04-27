# module (standard module )
# time
# random
# math




import random

# random(): generate the random float value between 0 and 1.0
out = random.random()
print(out)

# randrange() : return a integer value with given range
out = random.randrange(1, 20, 19)
print(out)

# randint: return a integer value with given range
out = random.randint(1, 20)
print(out)

# example number guessing
num_2 = random.randint(1, 100)
count = 0
while 1:
    count += 1
    num = int(input('enter the positive integer value between 1 and 100'))
    if num > num_2:
        print('too large')
    elif num < num_2:
        print('too small')
    else:
        print('right number with count score ', count)
        break



# choice : return single element with selected items
lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
out = random.choice(lst)
print(out)


# true number call
lst = list(range(1, 64))
while lst:
    input('please enter for next ')
    out = random.choice(lst)
    print(out)

    lst.remove(out)

print('all done ')











# random() : generate the random value between 0.0 and 1.0
import random

out = random.random()
print(out)

# randrange() : random number with range
import random

out = random.randrange(0, 10, 5)
print(out)

# randint(): random integer number with range

import random

out = random.randint(0, 10)
print(out)

# otp 6 digit
import random

out = int(random.random() * 10 ** 6)
print(out)

# choice()
h = [1, 3, 6, 3, 7, 9, 3, 6, 'hello']
out = random.choice(h)
print(out)

# game : number guess
import random as r
count = 0
sys_num = r.randint(0, 100)
while 1:
    count += 1
    num = int(input('enter the positive integer between 1 to 100'))
    if num < sys_num:
        print('user guessed number is lower ')
    elif num > sys_num:
        print('user guessed higher value ')
    else:
        print('right number with score count ', count)
        break

lst = list(range(1, 56))
while lst:
    input('enter for next person ')
    print(r.choice(lst))

