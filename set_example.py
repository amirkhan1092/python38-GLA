# initialization of set
# empty
s = set()  # using constructor
print(s, type(s))  # set() <class 'set'>
# k = {} # dict

# with single item
s = {7}

s = {'hello world'}
s = {True}
# mixed items
s = {1.78, None, 23, 'hello', (7, 6)}


# formation of set()
s = {0, 3, 5, 7, 8, 9, 2, 1, 'Hi', 'abchghghghhgghg', (5, 7)}
print(s)

# typecast with set
k = set('hello')
print(k)  # {'h', 'e', 'l', 'o'}

h = set(range(1, 20))
print(h)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}



# add() : to add the item in a set
k = {6, 8, 9, 4}
k.add(1)
k.add((23, 33))
print(k)
k.add(4.00)
k.add((6, 8, 9, 7))
print(k) # {True, 4, 6, 8, 9, None}


s = {2, 5}
s.add(2.0)
s.add(5.01)
print(s)  # {2, 5, 5.01}


s = set()
for i in range(5):
    s.add(int(input()))
print(s)


# update : add multiple items in a set()
k = {3, 5}
k.add('hello')  # {3, 5, 'hello'}
k.update('hello')  # {3, 5, 'hello', 'h', 'e', 'l', 'o' }
print(k) # {3, 5, 'hello', 'h', 'e', 'l', 'o' }

# remove(), discard(), clear() and pop()
k = {2, 5, 6}
k.remove(20)  # key error if item not found
print(k)


k = {2, 5, 6}
k.discard(10)   # no error if item not found
print(k)


k = {2, 6, 8}
k.clear() # clear the items
print(k)  # set()

k = {2, 6, 8, 'Hi', (2, 5)}
v = k.pop()
print('removed item ', v)
print(k)  # {6, 8, (2, 5), 'Hi'}


st = {4, 7}
st.add('hello')
st.update('gla uni ')
print(st, len(st))

# intersection()
S1 = {3, 7, 8, 9}
S2 = {11, 6, 3, 7}
V = S1.intersection(S2)  # method
V = S1 & S2  # expression
print(V)

# intersection_update()
S1 = {3, 7, 8, 9}
S2 = {11, 6, 3, 7}
S1.intersection_update(S2)
print(S1)


# union()
S1 = {3, 7, 8, 9}
S2 = {11, 6, 3, 7}
V = S1.union(S2)  # method
V = S1 | S2  # expression
print(V)


# difference()
S1 = {3, 7, 8, 9}
S2 = {11, 6, 3, 7}
D = S1.difference(S2)
D = S1 - S2
print(D)

# difference_update()
S1 = {3, 7, 8, 9}
S2 = {11, 6, 3, 7}
S1.difference_update(S2)
# S1 = S1 - S2
print(S1)


# symmetric_difference()
S1 = {3, 7, 8, 9}
S2 = {11, 6, 3, 7}
D = S1.symmetric_difference(S2)
D = S1 ^ S2
print(D)

# symmetric_difference_update()
S1 = {3, 7, 8, 9}
S2 = {11, 6, 3, 7}
S1.symmetric_difference_update(S2)
# S1 = S1 ^ S2
print(S1)  # {8, 9, 11, 6}

# issuperset(), #issubset(), isdisjoint()
S1 = {2, 5, 6, 9, 3, 4}
S2 = {3, 6, 9, 4}
k = S1.issuperset(S2)
print(k) # True


S1 = {2, 5, 6, 9, 3, 4}
S2 = {3, 6, 9, 4}
k = S2.issubset(S1)
print(k) # True

S1 = {2, 5, 6, 9, 3, 4}
S2 = {30, 60, 90, 14}
k = S1.isdisjoint(S2)
print(k)  # True


# difference_update()
# intersection_update()
# isdisjoint()
# symmetric_difference_update()
# discard()

















s = {2, 3, 5, 'hello', 'h', 'hsgdhgdhgwehdgwhdgwhghhgchdgchsdghsc', {2, 34}}
print(s)