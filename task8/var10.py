from itertools import product
abc = '0123'
combinations = product(abc, abc, abc, abc, abc)
bad_words = ['03', '30']
cnt = 0
for comb in combinations:
    comb = ''.join(comb)
    if comb.count('3') == 1 and comb[0] != '0':
        flag = True
        for b in bad_words:
            if b in comb:
                flag = False
        if flag == True:
            cnt += 1
print(cnt)