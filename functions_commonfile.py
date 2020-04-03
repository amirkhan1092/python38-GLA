# function
def Sum(n1, n2):
    return n1 + n2

num1 = 12
num2 = 21
res = Sum(num1, num2)
print(res)


def print_sum(n1, n2):
    print('Sum of two numbers is ', n1 + n2)

num1 = 12
num2 = 21
print_sum(num1, num2)

def type_sum(v1, v2):
    type1 = [int, list, str, tuple]
    type2 = [dict, set]
    if type(v1) in type1 and type(v2) in type1:
        res = value1 + value2
        return f'value is ordered or integer number, sum is {res}'
    else:
        value1.update(value2)
        return f'values are unordered merge file {value1}'

value1 = eval(input('enter the first value '))
value2 = eval(input('enter the second value '))
res = type_sum(value1, value2)
print(res)



