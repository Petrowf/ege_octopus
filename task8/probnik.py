"""
Сколько шестеричных четрыехзначных чисел, не содержащих цифру 4,
все цифры различны и никакие 2 четные или 2 нечетные цифры рядом не стоят
"""
from itertools import product

abc = '012345'
chet =  '024'
nechet = '135'
combs1 = product(chet, nechet, chet, nechet)
combs2 = product(nechet, chet, nechet, chet)

cnt = 0

for c in combs1:
    if '4' not in c and len(c) == len(set(c)) and c[0] != '0':
        cnt += 1

for c in combs2:
    if '4' not in c and len(c) == len(set(c)) and c[0] != '0':
        cnt += 1

print(cnt)