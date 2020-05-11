'''

input(): standard input read
print(): standard output write



file handling: reading and writing operation with file 

'''

 open(filename, mode)


f = open('test_file.txt', 'r')

data = f.read()

print(data)
f.close()












f = open('hello.txt', 'w')

f.write('this is my \nfirst time to write in my file\n')
f.write('second line')

f.close()



table
f = open('table.txt', 'w')
for i in range(1, 11):
    for k in range(1, 11):
        f.write(str(i*k)+'\t')

    f.write('\n')    


f.close()






 open(filename, mode(permission))


 w/wb : write only in text mode/ write only in binary
 w+/wb+ : write/read in text mode/ write/read in binary mode (file truncated)

 r/rb : read only in text mode/ read only in binary mode
 r+/rb+ : write/read in text mode/ write/read in binary mode

 a/ab : append mode for write only in text format/ binary format
 a+/ab+ : append mode for write/read in text format/binary




 create a file with student information


f = open('info.dat', 'w')

##f.closed  return bool type with file status
lst = ['Ankit kumar\n', 'section 3\n', 'rolln 20\n', 'address GLA\n']
if not f.closed:
    print('file succesfully opened ', f.name)
    f.writelines(lst)
    f.close()

    if f.closed:
        print('file saved ', f.name)

else:
    print('file not opened')




 read student info from file

 read() # it read the entire the data of the file from current location
f = open('info.dat', 'rb')

data1 = f.read(10)  # 10
data2 = f.read(2)   # 12
data3 = f.read() # 

##seek(offset, origin)
# origin
# 0 begin
# 1 current
# 2 last



data4 = f.read(2)


print('data1---', data1)
print('data2----', data2)
print('data3----', data3)
print('data4----', data4)
f.close()






f = open('info.dat', 'rb')

print('cursor loaction ', f.tell()) # 0

data = f.read(10)
data2 = f.read(3)

print('cursor loaction ', f.tell()) # 13


f.seek(6, 1)
print('cursor loaction ', f.tell())  # 19

f.close()



f = open('info.dat', 'rb')
f.seek(-5, 2)

data = f.read()

print(data)

f.close()


# readline(): read the current next line
f = open('info.dat', 'rb')

data1 = f.readline()
data2 = f.readline()
data3 = f.readline()


print(data1)
print(data2)
print(data3)

f.close()


# readlines(): list lines
f = open('info.dat', 'r')
data = f.readlines()
print(data)
f.close()


# next
f = open('info.dat', 'rb')

data1 = next(f)
data2 = next(f)
data3 = next(f)
data4 = next(f)
data5 = next(f) # EOF

print(data1)
print(data2)
print(data3)
print(data4)
print(data5)

f.close()



# iteration 
f = open('info.dat', 'rb')

for line in f:
    k = next(f)
    print(line)

f.close()   
      
    

with open('info2.dat', 'a+') as f:
    name = input('enter the name ')
    sec = input('enter the section ')
    roll = int(input('enter the rolln '))
    f.write(f'{name}\t{sec}\t{roll}')    
   


    
f = open('info2.dat', 'rb+')
f.seek(-4, 2)
f.write(b'30  ')
f.close()

    
       
    




























