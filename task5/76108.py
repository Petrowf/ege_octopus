for n in range(1, 1000):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n = '10' + bin_n + '0'
    else:
        sum_cifr = sum(map(int, list(bin_n)))
        bin_n = bin_n + bin(sum_cifr)[2:]
    r = int(bin_n, 2)
    if r > 600:
        print(r, n)