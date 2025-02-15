import itertools

abc1 = '02468'
abc2 = '13579'

combs1 = itertools.product(abc1, abc2, abc1, abc2, abc1, abc2)

combs2 = itertools.product(abc2, abc1, abc2, abc1, abc2, abc1)
cnt = 0

for comb in combs1:
    comb = ''.join(comb) #Перевод в строку
    if comb[-1] == '0' or comb[-1] == '5':
        if len(set(comb)) == len(comb): #Проверка на уникальность
            if comb[0] != '0':
                cnt += 1
for comb in combs2:
    comb = ''.join(comb)
    if comb[-1] == '0' or comb[-1] == '5':
        if len(set(comb)) == len(comb):
            if comb[0] != '0':
                cnt += 1


print(cnt)