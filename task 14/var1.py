for x in range(1, 5770):
    n = 9**2025 + 9**1000 - x
    n9 = ''
    while n != 0:
        n9 = str(n%9) + n9
        n = n // 9
    if n9.count('0') == 1026:
        print(x)