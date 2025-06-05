n = 3**333 + 3**22 - 9**111 - 8

n3 = ''
while n != 0:
    n3 = str(n%3) + n3
    n = n // 3

print(n3.count('2'))