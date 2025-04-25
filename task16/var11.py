def F(n):
    if n < 3:
        return 1
    if n%2 == 1:
        return F(n-1) + F(n-2)
    return sum([F(i) for i in range(1, n)])

print(F(24))