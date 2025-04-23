from itertools import product
abc = 'ДГИАШЭ'
combs = product(abc, repeat=5)
cnt = 0
for comb in combs:
    comb = ''.join(comb)
    if comb[0] not in 'ИАЭ' and comb[-1] not in 'ДГШ':
        cnt += 1
print(cnt)