from itertools import permutations

abc = '0123456789'
cnt = 0

for i in range(1, 11):
    combs = permutations(abc, i)
    for comb in combs:
        if i != 1 and comb[0] != '0' and comb[-1] in '05':
            cnt += 1
        elif i == 1 and comb[-1] in '05':
            print(comb)
            cnt += 1
            
print(cnt)