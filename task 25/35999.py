for m in range(0, 101, 2):
    for n in range(1, 100, 2):
        N = 2**m * 3**n
        if N >= 2*10**8 and N <= 4*10**8:
            print(N)