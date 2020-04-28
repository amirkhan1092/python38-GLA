# module (standard module )
# time
# random
# math

import random

# 1 random()  # generate the float number between 0 and 1.0
out = random.random()
print(out)


# example otp 6 digit
out = str(random.random())
print(out[-6:])

# randrange() :
out = random.randrange(1, 100, 2)  # 1, 6
print(out)


# randint:
out = random.randint(1, 10)
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


# choice

lst =  ['himanshu', 'deepak', 'karan', 'pawan']
out = random.choice(lst)
print(out)


lst  = [1, 2, 3, 4, 5, 6]
while 1:
    input('enter the for the next ')
    out = random.choice(lst)
    print(out)

random.shuffle(lst)
print(lst)


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



# choices : return list

lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
out = random.choices(lst, weights=[10, 1, 2, 3, 4], k=10)
print(out)

# shuffle
import random
def my_fun(ls):
    k = ls.copy()
    ls.clear()
    while k:
        x = random.choice(k)
        ls.append(x)
        k.remove(x)




lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
print(lst)
my_fun(lst)
print(lst)


# seed()
random.seed(101)
lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']

k = random.choice(lst)

print(k)