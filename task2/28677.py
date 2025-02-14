# выводим переменные по порядку
print('w', 'x', 'y', 'z', 'f')
bools = [0, 1]
#строим таблицу истиности
for w in bools:
    for x in bools:
        for y in bools:
            for z in bools:
                f = ((x <= y) or (y == w)) and ((x or z) == w)
                #фильтр на часть таблицы истиности
                if f == 1:
                    print(w, x, y, z, f)
