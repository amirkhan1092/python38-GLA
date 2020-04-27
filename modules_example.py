# module (standard module )
# time
# random
# math



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

