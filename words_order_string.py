# order of words in a string
# reverse
g = input('enter the string ')

l = g.split()  # split with whitespace separator may '\n',' ','\t' etc

l.reverse()

k = ' '.join(l)

print(f'original string:> {g}')
print(f'reverse string:> {k}')
# output
# original string:> this is python class
# reverse string:> class python is this