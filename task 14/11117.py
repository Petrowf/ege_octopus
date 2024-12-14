a = 4**2013 + 2**2012 - 16
n = a
a2 = ''

while n != 0:
    a2 = str(n % 2) + a2
    n = n // 2

print(a2.count('0'))