for n in range(2079, 10**9 + 1, 2079):
    ns = str(n)
    if ns[:2] == '33' and ns[-1] == '7' and ns[-4] == '2' and ns[-3] == '1':
        print(n, n/2079)