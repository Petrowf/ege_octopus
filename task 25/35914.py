cnt = 0
for i in range(45000000, 50000001):
    cnt_del = 0
    for j in  range(1, i//2, 2):
        if i % j == 0:
            cnt_del += 1
            if (i//j)%2 == 1:
                cnt_del += 1
        if cnt_del > 5:
            break
    if cnt_del == 5:
        print(i)
        cnt += 1
print(cnt)