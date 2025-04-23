def check(n):
    dels7 = []
    for i in range(2, int(n**0.5) + 4):
        if n % i == 0:
            j = n // i
            if (i % 10 == 7 and i != 7):
                dels7.append(i)
            if (j % 10 == 7 and j != 7):
                dels7.append(j)
    if len(dels7) != 0:
        return min(dels7)
    return False

for n in range(700000, 100000000):
    del7 = check(n)
    if del7 != False:
        print(n, del7)