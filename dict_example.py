
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
dct['name'] = 'Akshay'
dct['adress'] = 'GLA Mathura'
print(dct)

d = {'car':['alto', 'nano'], 'color':'white', 'model':1990,
     'speed':70, 23:'its number', (2, 4):'its tuple', 'car':'santro'}
print(d)
k = '1234*23)-87K81.2e'
ls = []
u = ''
for i in k:
    if i.isdigit() or i == '-' or i == '.':
        u += i
    else:
        ls.append(u)
        u = ''
print(ls)








