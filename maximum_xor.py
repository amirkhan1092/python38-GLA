k = list(map(int, input().split()))
ln = len(k)
mx = 0
for i in range(ln):
    for j in range(i+1, ln):
        mx = max(mx, k[i] & k[j])

print(mx)
