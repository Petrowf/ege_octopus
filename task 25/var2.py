def M(n):
    dels = []
    for m in range(2, int(n**(0.5)) + 1):
        if n % m == 0:
            dels.append(m)
            if n//m != m:
                dels.append(n//m)
    if len(dels) == 0:
        return 0
    return min(dels) + max(dels)

for n in range(1000000, 1000000000000000000000000000000000):
    if M(n) % 10  == 6:
        print(n, M(n))