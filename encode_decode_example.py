k = 'hello worldϪ'
out = k.encode('ascii',errors='replace')
print(k)
print(out)
print(out.decode('utf'))