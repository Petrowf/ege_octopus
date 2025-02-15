import itertools #Всегда

abc = '0123456' #Откуда берем цифры

combinations = itertools.product(abc, abc, abc, abc, abc, abc) #Все 6-тизначные комбинации
bad_words = ['20', '40', '60', '02', '04', '06'] #Последовательности которых быть не должно
cnt = 0 # счетчик

for comb in combinations: #Перебираем все комбинации
    comb = ''.join(comb) #Переводим комбинацию в строку
    if comb.count('0') == 1: #Первое условие
        flag = True #Флаг для проверки условия 2
        for word in bad_words:
            if word in comb:
                flag = False
        if flag == True: #Проверка условия 2
            cnt += 1

print(cnt)