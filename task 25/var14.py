def M(n):
    for i in range(2, int(n**(0.5)) + 2):
        if n % i == 0:
            j = n // i
            return j - i
    return 0
for n in range(860000, 100000000):
    if M(n) % 100 == 30:
        print(n, M(n))