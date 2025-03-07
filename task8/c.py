def podhod(xy):
    if (int(xy[0]) + int(xy[1])) % 2 == 0 and int(xy[1]) > int(xy[0]):
        return True
    elif (int(xy[0]) + int(xy[1])) % 2 == 1 and int(xy[0]) > int(xy[1]):
        return True
    else:
        return False

from itertools import product
abc = '012345678'
combs = product(abc, repeat=12)
cnt = 0

for comb in combs:
    comb = ''.join(comb)
    flag = False
    for i in range(0, 11):
        para = comb[i] + comb[i+1]
        if podhod(para):
            flag = True
    if flag == True:
        cnt += 1

print(cnt)