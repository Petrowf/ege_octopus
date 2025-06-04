R = []
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    #bin_n += str(n%2)
    if n%2 == 0:
        bin_n1 = bin_n + '0'
    else:
        bin_n1 = bin_n + '1'
    if bin_n.count('1') % 2 == 1:
        bin_n2 = bin_n1 + '1'
    else:
        bin_n2 = bin_n1 + '0'
    r = int(bin_n2, 2)
    R.append(r)
R_2023 = [r for r in R if r > 2023]
print(min(R_2023))