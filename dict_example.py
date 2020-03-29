

h = '''
List
Tuple
Dictionary
Sets

function(UDF, Built-in): arguments positional, keyword 
lambda function 
Module:
standard module: math, random, time, re
third party module: numpy, pandas

File handling: reading and writing operation with local files
Regular Expression: re 
Exception Handling

'''

# amirkhan1092.c1.biz/dict.pdf

# dictionary creation
# empty
d = {}
print(d, type(d))  # {} <class 'dict'>

d = dict()  # dict constructor
print(d, type(d))  # {} <class 'dict'>




H = ['Vaibhav', 20, 8.0, 'Sec 3', 'GLA']

D = {'name':['Vaibhav', 'sachine'], 'rolln':20, 'institute':'GLA', 'section': 'Sec 3'}

print(H[0])
print(D['name'])




# dictionary operation
dct = { 'rolln':30, 'cpi':8.0, 'section':'A', 'name':'akshay'}
print(dct, type(dct))


d = dct['name']  # element at given key
print(d) #accessing the element
d = dct['address']
print(d)  # keyError

dct['name'] = 'Abhinav'
dct['address'] = 'GLA University'
print(dct)



lst = ['hello', 'Hi', 'address', 'gla']
print(list(range(len(lst))))

# keys() : get all the keys of dict
dct = {'name': 'Govind', 'rolln':30, 'cpi':7.0, 'section':'A'}
out1 = dct.keys()
print(out1, type(out1))  # dict_keys(['name', 'rolln', 'cpi', 'section'])
# <class 'dict_keys'>

print(list(out1))  # ['name', 'rolln', 'cpi', 'section']

# values()
out2 = dct.values()
print(out2, type(out2))  # dict_values(['Govind', 30, 7.0, 'A'])
# <class 'dict_values'>



# update value at key
lst = [2, 4, 5]
lst[4] = 9

dct = {'name':'Govind', 'rolln':30, 'cpi':7.0, 'section':'E'}
dct['name'] = 'akshay'
dct['section'] = 'O'
dct['address'] = 'GLA University'
print(dct)

del dct['name']
print(dct)
dct['Name'] = 'akshay'
print(dct)



d = {1:0, 2:0, 3:0}
print(d)

# clear : to clear the dictionary object as empty
# to clear the items
d = {1:3, 0:43}
print(d)
print(id(d))
d.clear()
print(d)
print(id(d))




# copy
d = {1:  3, 0: 43}
y = d.copy()
y.clear()
print(y)
print(d)


# get
d = {'one': 3, 0: 43, (2, 4): 'tuple'}
out = d.get('second', 'NA')
print(out)  # NA


# fromkeys()
k = ['name', 'rolln', 'section', 'cpi']
d = dict.fromkeys(k, 0)
print(d)  # {'name': 0, 'rolln': 0, 'section': 0, 'cpi': 0}

d = {'entry1':{'name':'Sachin', 'section':'O'}, 'entry2':{'name':'Ravi', 'section':'T'}}

# 1,5,15,23,29,48,52,53,55

# items() : pure form dictionary
dct = {'name':'Govind', 'rolln':30, 'cpi':7.0, 'section':'E'}
pureform = dct.items()
print(pureform)
# [('name', 'Govind'), ('rolln', 30), ('cpi', 7.0), ('section', 'E')]



k = [(1, 6), (5, 4), (6, 7)]
d = dict(k)
print(d, type(d))
# {1: 2, 5: 4, 6: 7, 'H': 'i'} <class 'dict'>




# items()
D = {1:3, 4:0}
out = D.items()
print(out)  # dict_items([(1, 3), (4, 0)])

# pop()
D = {'name':'sachin', 'section':'O', 'rolln':30}
k = D.pop('rolln')
print(k)
print(D)

# popitems()
D = {'name':'sachin', 'section':'O', 'rolln':30}
k = D.popitem()
print(k)  # ('rolln', 30)

# update()
D1 = {'Name':'Sachin', 'Section':'O', 'Rolln':30}
D2 = {'CPI':9.0, 'Name':'Ravi'}
D1.update(D2)
print(D1)  # {'Name': 'Ravi', 'Section': 'O', 'Rolln': 30, 'CPI': 9.0}

# setdefault()

D1 = {'Name':'Sachin', 'Section':'O', 'Rolln':30}
D1.setdefault('rolln', 41)

print(D1)



















