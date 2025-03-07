for A in range(1, 16):
    flag = True
    for x in range(1, 16):
        if ((x&A != 0) <= ((x&10 == 0) <= x&3 != 0)) == False:
            flag = False
    if flag == True:
        print(A)