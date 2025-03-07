def de(n, m):
    if n%m == 0:
        return True
    return False

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = de(A, 40) and (de(780, x) <= ((not(de(A,x))) <= (not(de(180,x)))))
        if f == False:
            flag = False
    if flag == True:
        print(A)