s = '123456789'
print(list(s))
print(map(int, list(s)))
print(list(map(int, list(s))))
for n in range(4, 10000):
    s = '1' + '2'*n
    while '12' in s or '3322' in s or '2222' in s:
        if '12' in s:
            s = s.replace('12', '33', 1)
        if '2222' in s:
            s = s.replace('2222', '1', 1)
        if '3322' in s:
            s = s.replace('3322', '21', 1)
    s = list(map(int, list(s))) #list(s)- список букв, map(int, list(s)) - примняет int к каждому элементу list(s)
    if sum(s) == 218:
        print(n)