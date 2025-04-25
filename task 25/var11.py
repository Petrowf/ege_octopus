for n in range(2049, 10**9 + 1, 2049):
    n = str(n)
    if n[0] == '3' and n[1] == '2' and n[-1] == '4' and n[-3] == '1' and n[-4] == '2':
        n = int(n)
        print(n, n // 2049)