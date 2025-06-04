from itertools import product

abc = '012345678'
bad_words = ['15', '35', '75', '51', '53', '57']
cnt = 0
combs = product(abc, repeat=5)
for  comb in combs:
    comb = ''.join(comb)
    if comb[0] != '0' and all([bw not in comb for bw in bad_words]) and comb.count('5') == 1:
        cnt += 1

print(cnt)