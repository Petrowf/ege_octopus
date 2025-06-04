for A in range(300):
    flag = True
    for x in range(300):
        for y in range(300):
            f = (2*x + 3*y != 60) or (A >= x) or (A >= y)
            if f == False:
                flag = False

    if flag == True:
        print(A)