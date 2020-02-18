lst = [3, 0, 2, 8]

# 0, '', [], (), {}, set(), False, None
exe = 0
inc = 0
for i in lst:
    inc, exe = max(inc, exe), exe + i
print(max(inc, exe))
