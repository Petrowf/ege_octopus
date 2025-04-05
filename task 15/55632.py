for A in range(1000):
    flag = True
    for x in range(1000):
        f = ((x&116 != 0) or (x&92 != 0)) <= ((x&69 == 0) <= (x&A != 0))
        if f == False:
            flag = False
    if flag == True:
        print(A)