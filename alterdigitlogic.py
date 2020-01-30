n = int(input())  # number of test cases
for i in range(n):
    out = []
    vt = list(map(int, input().split()))
    lst = input().split()

    for k in lst:
        if len(k) >= 2:
            if 1 == abs(int(k[0]) - int(k[1])) :
                if vt[1] > int(k):
                    out.append(int(k))

    print(*out)