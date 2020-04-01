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
k.add(True)
k.add(4.00)
k.add((6, 8, 9, 7))
print(k) # {True, 4, 6, 8, 9, None}



s = set()
for i in range(5):
    s.add(int(input()))
print(s)


# update : add multiple items in a set()
k = {3, 5}
k.update(range(6, 11))
print(k)

st = {4, 7}
st.add('hello')
st.update('gla uni ')
print(st, len(st))



# intersection_update
S1 = {3, 7, 8, 9, 11, 6, 7, 89, 56}
S2 = {11, 6, 3, 7}

k = S1.issuperset(S2)
print(k)





















s = {2, 3, 5, 'hello', 'h', 'hsgdhgdhgwehdgwhdgwhghhgchdgchsdghsc', {2, 34}}
print(s)