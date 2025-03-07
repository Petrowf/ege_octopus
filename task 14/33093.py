n = 81**15 + 3**22 - 27
n9 = ''

while n != 0:
    n9 = str(n%9) + n9
    n = n//9

print(n9.count('8'))