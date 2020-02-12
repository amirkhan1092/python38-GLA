
# dictionary creation empty
d = {}
print(d, type(d))  # {} <class 'dict'>

d = dict()  # dict constructor
print(d, type(d))  # {} <class 'dict'>


# dictionary operation

dct = { 'rolln':30, 'cpi':8.0, 'section':'A', 'name':'akshay'}
print(dct, type(dct))
# accessing the element
d = dct['name']  # element at given key
print(d)

# keys() : get all the keys of dict
dct = {'name':'Govind', 'rolln':30, 'cpi':7.0, 'section':'E'}
out1 = dct.keys()
print(out1)  # dict_keys(['name', 'rolln', 'cpi', 'section'])

out2 = dct.values()
print(out2, type(out2))  # dict_values(['Govind', 30, 7.0, 'E']) <class 'dict_values'>

# update value at key
dct = {'name':'Govind', 'rolln':30, 'cpi':7.0, 'section':'E'}
dct['name'] = 'akshay'
dct['adress'] = 'GLA Mathura'
print(dct)

d = {1:0, 2:0, 3:0}
print(d)

# clear : to clear the dictionary object as empty
d = {1:3, 0:43}
d.clear()
print(d)





p = 1,7,10,18,44,46,52,54

# copy
d = {1:3, 0:43}
t = d.copy()
t['next'] = 'data from user '


print(t)
print(d)


# get
d = {1:3, 0:43, (2, 4):'tuple'}
out = d.get(1)
print(out)

# fromkeys()
k = ['name', 'rolln', 'section', 'cpi']
d = dict.fromkeys(k, 0)
out = d.items()
print(out)

d = {'entry1':{'name':'Sachin', 'section':'O'}, 'entry2':{'name':'Ravi', 'section':'T'}}

# 1,5,15,23,29,48,52,53,55

k = [(1, 2), (5, 4), (6, 7), 'Hi']
d = dict(k)
print(d, type(d))


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



















