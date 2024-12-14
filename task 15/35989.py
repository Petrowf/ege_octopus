for A in range(1000):
    flag = True
    for x in range(1000):
        if not((x & 73 ==0) <= ((x & 28 != 0) <= (x & A != 0))):
            flag = False
    if flag == True:
        print(A)