abc = [i for i in range(37)]
for x in abc:
    for y in abc:
        n = 2*37**7 + 1*37**6 + x*37**5 + 4*37**4 + 5*37**3 + 7*37**2 + y*37 + 9
        if n % 36 == 0:
            print(x, y)

    print(36*37 + 8)