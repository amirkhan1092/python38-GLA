k = input('enter the string ')
out = ''

for i in k:
    if i not in out:
        out += i

print(out)

