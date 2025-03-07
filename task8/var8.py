from itertools import product

abc = 'агеилнрт'

combs = product(abc, abc, abc, abc, abc)

cnt = 0
i = 1
for comb in combs:
    comb = ''.join(comb)
    if i%2==1 and comb[0]!='т' and (1 <= comb.count('н') <= 2):
        cnt += 1
    i += 1

print(cnt)