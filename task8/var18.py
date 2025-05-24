from itertools import product
abc = [0, 1, 2, 3, 4]
combs = product(abc, repeat=3)
cnt = 0
for comb in combs:
    if comb[0] > comb[1] > comb[2]:
        cnt += 1
print(cnt)