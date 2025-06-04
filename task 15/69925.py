def DEL(n, m):
    if n % m == 0:
        return True
    else:
        return False

B = range(70, 91)
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):

        f = DEL(x, A) or ((x in B) <= (not(DEL(x, 22))))
        if f == False:
            flag = False
    if flag == True:
        print(A)
