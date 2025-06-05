f = {}

for n in range(1, 7):
    if n <= 2:
        f[n] = 2
    else:
        f[n] = 3*f[n-1] - f[n-2]

print(f[6])