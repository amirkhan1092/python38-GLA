# module (standard module )
# time
# random
# math

# random

import random

# 1. random() : to generate the random value between 0 and 1
out = random.random()
print(out)


# Example OTP using random
d = int(input('enter width of OTP '))
out = str(random.random())[-d:]
print(out)


# 2. randrange()  : return integer with given range
out = random.randrange(1, 20, 5)
print(out)



# 3. randint() : return integer with given range no manual step size
out = random.randint(1, 20)
print(out)
print(random.randint(1, 20))


# 4. choice() : return element from selected items
lst = ['abhishek', 'arpit', 'ghanshyam', 'aman', 'archit', 'chetan']
out = random.choice(lst)
print(out)


# number guess

sys = random.randint(1, 100)
count = 0
while 1:
    count += 1
    num = int(input('enter the number between 1 and 100 '))
    if sys > num:
        print('too small ')
    elif sys < num:
        print('too large')
    else:
        print('right number with score count ', count)
        break


# 5 choices : return list of choice from selected
lst = ['abhishek', 'arpit', 'ghanshyam', 'aman', 'archit', 'chetan']
out = random.choices(lst, weights=[10, 1, 5, 6, 6, 1], k=10)
print(out)

# 6 sample : return list of items from selected
lst = ['abhishek', 'arpit', 'ghanshyam', 'aman', 'archit', 'chetan']
out = random.sample(lst, k=3)
print(out)


# 7 shuffle: to shuffle the list
lst = ['abhishek', 'arpit', 'ghanshyam', 'aman', 'archit', 'chetan']
print(lst)  # before shuffle
random.shuffle(lst)
print(lst)  # after shuffle

# example shuffle the list without shuffle method
lst = ['abhishek', 'arpit', 'ghanshyam', 'aman', 'archit', 'chetan']
new_lst = lst.copy()
lst.clear()
while new_lst:
    tt = random.choice(new_lst)
    lst.append(tt)
    new_lst.remove(tt)
print(lst)





# 8 seed()
random.seed(110)
lst = ['abhishek', 'arpit', 'ghanshyam', 'aman', 'archit', 'chetan']
out1 = random.choice(lst)
print(out1)



# 9 getrandbits
import random
out = random.getrandbits(2)
print(out)



# 10 uniform

out = random.uniform(1, 2)
print(out)

# 11 triangular
out = random.triangular(10, 30, 50)
print(out)






# getrandbits()

out = random.getrandbits(3)
print(out)



print(random.triangular(10, 20, 18))

import math
l = math.floor(12.91)
print(l)


import time
print(time.asctime())







import random

# 1 random()  # generate the float number between 0 and 1.0
out = random.random()
print(out)


# example otp 6 digit
out = str(random.random())
print(out[-6:])

# 2 randrange() : return integer with given range
out = random.randrange(1, 100, 2)  # 1, 6
print(out)


# 3 randint: return integer with given range
out = random.randint(1, 100)
print(out)


# example : guess the number

sys_num = random.randint(1, 100)
count = 0
while 1:
    count += 1
    num = int(input('enter the number between 1 and 100'))
    if num > sys_num:
        print('too large')
    elif num < sys_num:
        print('too small')
    else:
        print('right number with score count ', count)
        break


from math import *
a = int(input('enter the value '))

out = int(log(a, 256)) + 1
print(out)




import math

out = math.ceil(12.5)
print(out)

out = math.floor(12.5)
print(out)

import time
out = time.time()
print(out)

out = time.asctime()
print(out)

# st1 = 'ACB'
# st2 = 'ABC'
# st1 = st1.lower()
# st2 = st2.lower()
#
# print(st2 in st1)




# def my_fun(fun1):
#     def wrapper():
#         print('hello')
#         fun1()
#         print('welcome')
#     return wrapper
# def second():
#     print('this is second')
#
#
# a = my_fun(second)
# a()
#









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



# 3 choice : return single element with selected items
import random
lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
out = random.choice(lst)
print(out)


# 4 choices : return list of items
import random
lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
out = random.choices(lst, weights=[1, 10, 3, 8, 2], k=5)
print(out)


# 5 sample
lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
out = random.sample(lst, k=4)
print(out)

# 6 shuffle: to shuffle the list
import random
lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
print(lst)  # before shuffle
random.shuffle(lst)
print(lst)  # after shuffle


# shuffle the list without shuffle method in random
import random
def my_fun(ls):
    tc = ls.copy()
    ls.clear()
    while tc:
        y = random.choice(tc)
        ls.append(y)
        tc.remove(y)


lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
print(lst)  # before shuffle
my_fun(lst)
print(lst)  # after shuffle


# 7 seed()
import random
random.seed(20)


lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
out1 = random.choice(lst)
print(out1)


# sample
lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
out = random.sample(lst, k=5)
print(out)

# shuffle
lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
random.shuffle(lst)
print(lst)

# 8 getrandbits
ut = random.getrandbits(8)
print(ut)


#
print(random.triangular(1, 20, 15))

print(random.uniform(1, 2))


# math
import math
print(math.pi)

print(math.floor(23.99))
print(math.ceil(23.0))

import time
out = time.time()
print(out)

print(time.asctime())

# file handling
# exception handling









