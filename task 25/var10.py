for n in range(123, 10**8 + 1, 123):
    str_n = str(n)
    if str_n[0] == '3' and str_n[1] == '2' and str_n[-1] == '3' and str_n[-2] == '2' and str_n[-3] == '8':
        print(n, n // 123)