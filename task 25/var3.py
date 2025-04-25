def R(n):
    r = 0
    for i in range(2, int(n**0.5) + 2):
        if n % i == 0:
            r += i
            r += n // i
    return r

for n in range(800000, 100000000):
    r = R(n)
    if r % 10 == 3:
        print(n, r)