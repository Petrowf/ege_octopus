f = {1: 2,
     2: 2}

for n in range(3, 7):
    f[n] = 3*f[n-1] - f[n-2]

print(f[6])