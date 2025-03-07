from itertools import  product

abc = '01234567'

combs = product(abc, repeat=5)
cnt = 0
bad_words = ['14', '41', '34', '43', '54', '45', '74', '47']
for comb in combs:
    comb = ''.join(comb)
    if comb[0] != '0' and comb.count('4') == 2:
        flag = True
        for bw in bad_words:
            if bw in comb:
                flag = False
        if flag == True:
            cnt += 1
print(cnt)