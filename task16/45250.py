f = {1: 2,
     2: 2}

for n in range(3, 33):
    if n % 2 == 0:
        f[n] = f[n-2] + f[n-1] - n
    else:
        f[n] = f[n-1] - f[n-2] + 2*n

print(f[32])
