def R(n):
    r = 0
    for i in range(2, int(n**0.5) + 3):
        if n % i == 0:
            j = n // i
            r += i
            if i != j:
                r += j
    return r

cnt = 0
n = 900001
while cnt != 5:
    r = R(n)
    if r % 10 == 5:
        cnt += 1
        print(n, r)
    n += 1
