# 1*4182?7 / 1991 < 10^10

for i in range(10):
    a = int('14182' + str(i) + '7')
    if a % 1991 == 0:
        print(a)

for i in range(10):
    for j in range(10):
        a = int('1' + str(i) + '4182' + str(j) + '7')
        b = int('10' + str(i) + '4182' + str(j) + '7')
        c = int('100' + str(i) + '4182' + str(j) + '7')
        if a % 1991 == 0:
            print(a)
        if b % 1991 == 0:
            print(b)
        if c % 1991 == 0:
            print(c)

for i in range(10, 100):
    for j in range(10):
        a = int('1' + str(i) + '4182' + str(j) + '7')
        b = int('10' + str(i) + '4182' + str(j) + '7')
        if a % 1991 == 0:
            print(a)
        if b % 1991 == 0:
            print(b)


for i in range(100, 1000):
    for j in range(10):
        a = int('1' + str(i) + '4182' + str(j) + '7')
        if a % 1991 == 0:
            print(a)

