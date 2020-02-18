
# Python Loop
1
# 1. for loop
'''
The for statement in Python differs a bit from what you may be used to in C or Pascal. 
Rather than always iterating over an arithmetic progression of numbers, 
or giving the user the ability to define both the iteration step and halting condition (as C), 

Python’s for statement iterates over the items of any sequence 
(a list or a string), in the order that they appear in the sequence. 
For example :

'''

vs = 'hello python'
for i in vs:
    print(i)
vs = 'hello python'
for i in vs:
    if i == ' ':
        break
    print(i)
else:
    print('loop complete ')


#The break statement, breaks out of the innermost enclosing for or while loop
# break just stop the iteration within the loop



#The continue statement, continues with the next iteration of the loop:

for i in range(10):
    print('single ',i)
    if i > 5:
        continue
    print('with expression', 2*i+2)
else:
    print('loop completed ')


# pass : pass just a keyword. it pass the instruction (do nothing). use to maintain the scope
def fun(r):
    pass

h = fun(34)

while 1:
    pass


for i in range(10):
    if i == 2:
        pass
    else:
        print(i**2)


def abcd(a, l=[]):
    for i in range(a):
        l.append(i*i)
    print(l)

