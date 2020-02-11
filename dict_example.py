
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

d = {'car':['alto', 'nano'], 'color':'white', 'model':1990,
     'speed':70,            23:'its number',            (2, 4):'its tuple'
     }
print(d)

# clear : to clear the dictionary object as empty
d = {1:3, 0:43}
d.clear()
print(d)


# copy
d = {1:3, 0:43}
t = d.copy()
t['next'] = 'data from user '

print(t)
print(d)


# get
d = {1:3, 0:43, (2, 4):'tuple'}
out = d.get((2, 4))
print(out)

# fromkeys()
k = ['name', 'rolln', 'section', 'cpi']
d = dict.fromkeys(k)
print(d)

# 1,5,15,23,29,48,52,53,55

d = {1:[2, 4]}
d[1].append(10)
print(d)
















