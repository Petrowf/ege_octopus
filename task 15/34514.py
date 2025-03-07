for A in range(64):
    flag = True
    for x in range(64):
        f = (x&49 != 0) <= ((x&41==0) <= (x&A != 0))
        if f == False:
            flag = False
    if flag == True:
        print(A)