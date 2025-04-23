"""
Определите количество четырехзначных чисел,
записанных в десятичной системе счисления,
в записи которых все цифры различны и
никакие две чётные и две нечётные цифры не стоят рядом.
"""

from itertools import product
chet = '02468'
nechet = '13579'

combs1 = product(chet, nechet, chet, nechet)
combs2 = product(nechet, chet, nechet, chet)

cnt = 0

for c in combs1:
    if c[0] != '0' and len(c) == len(set(c)):
        cnt += 1

for c in combs2:
    if c[0] != '0' and len(c) == len(set(c)):
        cnt += 1

print(cnt)