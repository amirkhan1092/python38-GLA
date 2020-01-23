intab = 'aaeoa'
outab = '12345'

trans = str.maketrans(intab, outab)

st = 'this is python class'
out = st.translate(trans)
print(out)