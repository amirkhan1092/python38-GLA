

# example 1
import time
def countdown(x):  # x = 4
    if x == 0:
        pass
    else:
        print(x)
        countdown(x-1)

v1 = time.time()
countdown(1000)
v2 = time.time()
print(v2-v1)
print('Happy Recursion Day')
out1 = 0.014958620071411133


# countdown using iteration
def countdown(x):  # x = 4
    for  i in range(x, 0, -1):
        print(i)


v1 = time.time()
countdown(1000)
v2 = time.time()
print(v2-v1)
out2 = 0.011011362075805664

print(out1-out2)




def fact(n):
    p = 1
    if n == 0:
        return 1
    else:
        p =  n*fact(n-1)


num = int(input('enter the number '))
out = fact(0)
print('factorial of given number is ', out)


