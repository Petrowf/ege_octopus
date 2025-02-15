cnt = 0

for i in range(100, 1000):
    stroka = ''
    n = i
    while n != 0:
        stroka = str(n%4) + stroka
        n = n // 4
    print(stroka)
    if len(set(stroka)) == len(stroka) and stroka == sorted(stroka):
        cnt += 1
print(cnt)
