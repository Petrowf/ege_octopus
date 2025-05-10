def del7(n):
    dels_7= []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            if i % 10 == 7 and i != 7:
                dels_7.append(i)
            if j % 10 == 7 and j != 7 and j != i:
                dels_7.append(j)
    if len(dels_7) > 0:
        return min(dels_7)
    else:
        return False

n = 1125001
cnt = 0
while cnt != 5:
    d = del7(n)
    if d != False:
        print(n, d)
        cnt += 1
    n += 1