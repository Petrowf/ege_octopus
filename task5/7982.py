for n in range(100, 1000):
    first = n // 100
    second = (n // 10) % 10
    third = n % 10
    x = first + second
    y = second + third
    R = str(max(x, y)) + str(min(x, y))
    if R == '159':
        print(n)