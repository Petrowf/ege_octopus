cnt = 0
for i in range(2024, 10**10+1, 2024):
    s = str(i)
    if s[0] == '1' and s[2:6] == '2157' and s[-1] == '4':
        print(s, i//2024)
