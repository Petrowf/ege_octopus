for A in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not((x+ 2*y < A) or (y > x) or (x > 20)):
                flag = False
    if flag == True:
        print(A)