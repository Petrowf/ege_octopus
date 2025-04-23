for n in range(1, 1000):
    n2 = ''
    n10 = n
    while n10 != 0:
        n2 = str(n10%2) + n2
        n10 = n10 // 2
    s = sum(map(int, list(n2)))
    if s % 2 == 0:
        n2 = n2 + '0'
        n2 = '10' + n2[2:]
    else:
        n2 = n2 + '1'
        n2 = '11' + n2[2:]
    r = int(n2, 2)
    if r > 480:
        print(n, n2, r)