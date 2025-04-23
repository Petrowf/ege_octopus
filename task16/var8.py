f = {1: 1,
     2: 2}

for n in range(3, 2025):
     f[n] = n*(n-1) + f[n-1] - f[n-2]

print(f[2024] + f[2020] - f[2019])