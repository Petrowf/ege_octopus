for i in range(3*10**8, 4*10**8):
    d= set()
    cnt = 0
    for j in range(i - 1, int(i**0.5)+1, - 1):
        if i % j == 0:
            d.add(j)
            d.add(i//j)
    if len(d) >= 5:
        print(sorted(d)[-5])
        cnt += 1
    if cnt == 5:
        break


