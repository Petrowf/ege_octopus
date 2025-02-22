from itertools import product
abc = '0123'
cnt = 0
combs = product(abc, repeat=3)
for comb in combs:
    comb = ''.join(comb)
    if len(set(comb)) == len(comb):
        if comb == ''.join(sorted(comb)[::-1]):
            cnt += 1

print(cnt)