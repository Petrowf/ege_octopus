from itertools import product
abc = '123456'
combs = product(abc, repeat=4)
cnt = 0
for comb in combs:
    if comb.count('3') == 1 and sum([comb.count(ch) for ch in '246']) <= sum([comb.count(ch) for ch in '135']):
        cnt += 1

print(cnt)