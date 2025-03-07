from itertools import product
abc1 = '0246'
abc2 = '357'
cnt = 0

combs = product(abc1, abc2, abc1, abc2, abc1)
for comb in combs:
    comb = ''.join(comb)
    if len(set(comb)) == len(comb) and comb[0] != '0':
        cnt += 1

combs = product(abc2, abc1, abc2, abc1, abc2)
for comb in combs:
    comb = ''.join(comb)
    if len(set(comb)) == len(comb):
        cnt += 1

print(cnt)
