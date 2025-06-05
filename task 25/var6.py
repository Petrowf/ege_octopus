for n in range(12007, 10**10 + 1, 12007):
    str_n = str(n)
    if str_n[0] == '9' and str_n[-1] == '1' and str_n[-3] == '1' and str_n[-4] == '0' and str_n[-5] == '0':
        print(n, n // 12007)