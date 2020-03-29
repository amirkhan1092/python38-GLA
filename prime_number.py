def prime_or_not(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True
# filer prime numbers
lst = [2, 4, 7, 3, 14, 9, 10, 67]
res = []
for n in lst:
    if prime_or_not(n):res.append(n)
print(res)