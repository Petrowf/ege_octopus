f = {1: 1}
for n in range(2, 3001):
    f[n] = n + f[n-1]
print(f[3000] - f[2000])