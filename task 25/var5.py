for n in range(31007, 10**10 + 1, 31007):
    n = str(n)
    if n[0] == '1' and n[-1] == '9' and n[-3] == '5' and n[-5] == '4' and n[-6] == '3':
        n = int(n)
        print(n, n // 31007)