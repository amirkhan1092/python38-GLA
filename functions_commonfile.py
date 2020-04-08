# function
def Sum(n1, n2):
    return n1 + n2

num1 = 12
num2 = 21
res = Sum(num1, num2)
print(res)

# function2
def print_sum(n1, n2):
    print('Sum of two numbers is ', n1 + n2)

num1 = 12
num2 = 21
print_sum(num1, num2)


def type_sum(v1, v2):
    type1 = [int, list, str, tuple]
    type2 = [dict, set]
    if type(v1) in type1 and type(v2) in type1:
        res = v1 + v2
        return f'value is ordered or integer number, sum is {res}'
    else:
        v1.update(v2)
        return f'values are unordered merge file {v1}'
value1 = eval(input('enter the first value '))
value2 = eval(input('enter the second value '))
print(type_sum(value1, value2))



# positional
def add( y, k = 0):
    print('first argv ', k)
    print('second argv ', y)

add(5,)

# optional values
h, k, *u = (6, 9, 78, 7)

#
# def type_sum(a, b):
#     if type(a) == dict or type(a) == set:
#         a.update(b)
#         return f'values are unordered and merge value is {a}'
#     else:
#         re = a + b
#         return f'values are ordered and sum/merge is {re}'
#
# v1 = eval(input('enter the first value '))
# v2 = eval(input('enter the second value '))
# c = type_sum(v1, v2)



# arguments in Python Function
# default arguments
def add(a, b=0): # right
    return a + b
k = add(8)
print(k)

def add(a=0, b): # error
    return a + b
k = add(7, 8)
print(k)

# built-in Example
print(int('67', 8))  # 8 is default argv



# positional arguments
def add(a, b):
        print('at first position ', a)
        print('second position ', b)
k = add( 30, 'rishabh')
print(k)




# optional positional arguments
def add(a, b, *t):
    print('at first position ', a)
    print('second position ', b)
    print('optional argv', t)

k = add('rishabh', 80)
print(k)



def optional_sum(*opt, a=0, b=0):
    return sum(opt)

h = optional_sum(7, 8, 9, 5, 4, 4, a = 7, b= 78)
print(h)


print(8, 'hello', 9.0, 89, sep='*')



def disp(*t, sap=' ', nnd='' ):  # t = ('hello', 8, 60, 8.0)
    k = sap.join(map(str, t))
    print(k,end='')
    print(nnd, end='')

disp("hello", 8, 60, 8.0, end='\n')
disp("Next command ")



# keyword arguments
def add(a, b):
    return a**2, b**3

sqr, cube = add(b=9, a=7)
print('square',sqr)
print('cube', cube)

# optional Keyword arguments
def temp(**dt):
    re = '''
    Name : {}
    Roll number : {}
    Section : {}
    Address : {}
    '''. format(dt.get('name'), dt.get('rolln'), dt.get('sec'), dt.get('address'))
    return re

t = temp( Sec='O', AddRess="GLA", Name='Rishabh', cpi=7.9, father="Mr xyz")
print(t)


























