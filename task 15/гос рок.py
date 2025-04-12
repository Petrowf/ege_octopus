for A in range(300):
    flag = True
    for x in range(300):
        for y in range(300):
            f = (5 < y) or (x > 32) or (x + 2*y < A)
            if f == False:
                flag = False
    if flag == True:
        print(A)