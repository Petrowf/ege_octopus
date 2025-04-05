for A in range(300):
    flag = True
    for x in range(300):
        for y in range(300):
            f = (x + 2*y > A) or (x > 13) or (y < 44)
            if f == False:
                flag = False
    if flag == True:
        print(A)