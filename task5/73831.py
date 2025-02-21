for n in range(1, 100000000000):
    k = 2
    dec_n = n
    bin_n = ''
    #перевод в k-ичную систему счисления
    while dec_n != 0:
        bin_n = str(dec_n%k) + bin_n
        dec_n = dec_n // k
    colvo_edinic = bin_n.count('1')
    colvo_nul = bin_n.count('0')

    bin_1 = ''
    bin_0 = ''
    while colvo_edinic != 0:
        bin_1 = str(colvo_edinic%k) + bin_1
        colvo_edinic = colvo_edinic // k

    while colvo_nul != 0:
        bin_0 = str(colvo_nul%k) + bin_0
        colvo_nul = colvo_nul // k

    bin_r = bin_1 + bin_0
    #перевод из к-ичной в десятичную
    r = int(bin_r, k)
    if r == 214:
        print(n)
        break

