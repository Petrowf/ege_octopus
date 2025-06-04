D = range(17, 59)
C = range(29, 81)
A_len = []

for a1 in range(-100, 101):
    for a2 in range(a1 + 1, 102):
        A = range(a1, a2 + 1)
        flag = True
        for x in range(-100, 102):
            f = (x in D) <= (((x not in C) and (x not in A)) <= (x not in D))
            if f == False:
                flag = False
        if flag == True:
            A_len.append(len(A) - 1)
print(A_len)
print(min(A_len))

