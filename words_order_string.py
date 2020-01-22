# # order of words in a string
# # reverse
# g = input('enter the string ')
#
# l = g.split()  # split with whitespace separator may '\n',' ','\t' etc
#
# l.reverse()
#
# k = ' '.join(l)
#
# print(f'original string:> {g}')
# print(f'reverse string:> {k}')
#
# # output
# # original string:> this is python class
# # reverse string:> class python is this
#
#
# # reverse words character
# st = input('add paragraph ')
#
# ls = st.split()  # list of words
# # p = []
# c = 0
# for k in ls:
#     # p.append(k[::-1])
#     ls[c] =  k[::-1]
#     c += 1
# out = ' '.join(ls)
# print(f'original string:> {st}')
# print(f'reverse string:> {out}')
#

h = input('enter the string')
ls = h.split()

st = sorted(ls,key = len)

print('word_max',st[-1])
print('word_min',st[0])







