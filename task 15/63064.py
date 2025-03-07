for A in range(1, 1000):
    flag = True
    for x in range(1000):
        if (((x&45 > 0) or (x&89 > 0)) <= (x&A > 0)) == False:
            flag = False
    if flag == True:
        print(A)