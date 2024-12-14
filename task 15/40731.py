P = range(19, 85)
Q = range(4, 52)
As = []
for A1 in range(-100, 100):
    for A2 in range(-100, 100):
        A = range(A1, A2)
        flag = True
        for x in range(-100, 100):
            if not((x in Q) <= ((not(x in P)) <= (not((x in Q) and (not(x in A)))))):
                flag = False
        if flag == True:
            As.append(len(A))

print(min(As))