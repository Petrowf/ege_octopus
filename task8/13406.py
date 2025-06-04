from itertools import product
abc = 'ABCDXYZ'
combs = product(abc, repeat=4)
cnt = 0
for comb in combs:
    if comb[0] in "XYZ" and comb[1] not in "XYZ" and comb[2] not in "XYZ" and comb[3] not in "XYZ":
        cnt += 1

print(cnt)