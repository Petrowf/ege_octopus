for p in range(5, 30):
    for x in range(p):
        for y in range(p):
            a = 3*p + 2
            b = 1*p + 4
            n = x*p**2 + y*p + 2
            if a*b == n:
                print(y*p + x, p)
