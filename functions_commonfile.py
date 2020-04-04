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







def add( y, k = 0):
    print('first argv ', k)
    print('second argv ', y)

add(5,)

h, k, *u = (6, 9, 78, 7)



def add(a, b):
    if type(a) in [dict, set]:
        a.update(b)
        return f'values are unordered and addition/merge values is {a}'
    else:
        c = a + b
        return f'value are ordered and addition is {c}'

v1 = eval(input('enter the value 1'))
v2 = eval(input('enter the value 1'))
c = add(v1, v2)
print(c)





















