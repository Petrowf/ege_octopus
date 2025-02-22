from itertools import product #всегда

abc = '012345' #какие цифры или буквы есть

bad_words = ['10', '01', '30', '03', '50', '05'] # каких не должно быть

combs = product(abc, abc, abc, abc, abc, abc) #составляем комбинации
cnt = 0 # счетчик

for comb in combs: # Перебираем комбинации
    comb = ''.join(comb) # Превращаем в строку
    if comb[0] != '0' and comb.count('0') == 1: #Проверяем условия
        flag = True # флаг проверки отстутсвия
        for bw in bad_words: # все плохое
            if bw in comb: # если есть
                flag = False # опускаем флаг
        if flag == True: # если флаг поднят
            cnt += 1 # прибавляем к счетчику

print(cnt) #выводим счетчик
