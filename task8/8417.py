from itertools import product

abc = "ЯРОСЛАВ"
combs = product(abc, repeat=5)
bad = ['ЯО', "ЯА", "ОА", "ОЯ", "АЯ", "АО"]
cnt = 0
for comb in combs:
    comb = ''.join(comb)
    if1 = len(set(comb)) == len(comb)
    if2 = (comb.count('Р') + comb.count('С') + comb.count('Л') + comb.count('В')) > (comb.count('Я') + comb.count('О') + comb.count('А'))
    if3 = all([ch not in comb for ch in bad])
    if if1 and if2 and if3:
        cnt+=1

print(cnt)
