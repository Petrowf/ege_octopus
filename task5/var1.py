for n in range(1, 1000):
    # перевод в двоичную систему счисления
    bin_n = bin(n)[2:]
    if n%2 == 0:
        bin_n = bin_n.replace('1', '11')
    else:
        bin_n = bin_n.replace('0', '00')

    r = int(bin_n, 2)
    if r > 70:
        print(n)
