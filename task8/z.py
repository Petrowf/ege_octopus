from itertools import product
abc = 'андрей'
combs = product(abc, repeat=5)
cnt = 0
for comb in combs:
    comb = ''.join(comb)
    if comb[0] != 'й' and (comb.count('а') >= 1 or comb.count('е') >= 1):
        cnt += 1
print(cnt)