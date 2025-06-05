def F(n):
    dels = []
    for i in range(2, int(n**0.5) + 2):
        if n % i == 0:
            #Если делитель должен быть простым
            # cnt_dels = 0
            # for k in range(2, int(i**0.5) + 2):
            #     if i % k == 0:
            #         cnt += 1
            # if cnt != 0:
            dels.append(i)
            j = n//i
            if i != j:
                # Если делитель должен быть простым
                # cnt_dels = 0
                # for k in range(2, int(j**0.5) + 2):
                #     if j % k == 0:
                #         cnt += 1
                # if cnt != 0:
                dels.append(j)
    if len(dels) == 0:
        return False
    f = max(dels) - min(dels)
    if f != 0 and f % 11 == 0:
        return f
    else:
        return False

for n in range(850001, 100000000):
    f = F(n)
    if f != False:
        print(n, f)