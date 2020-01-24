intab = 'abcief'
outab = '123456'

trans = str.maketrans(intab,outab)

k = 'this is python class at 10:20 AM'
out = k.translate(trans)
print(out)