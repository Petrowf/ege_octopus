for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = (120%A == 0) and ((x%36 == 0) <= ((x%A != 0) <= (x%45 != 0)))
        if f == False:
            flag = False
    if flag == True:
        print(A)