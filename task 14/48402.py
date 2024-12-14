for x in range(1, 2031):
    a = 3**100 - x
    n = a
    a3 = ''
    while a != 0:
        a3 = str(a % 3) + a3
        a = a // 3
    if a3.count('0') == 2:
        print(x)
