F = {1: 1,
     2: 2}
for i in range(3, 2025):
    F[i] = i*(i-1) + F[i - 1] - F[i - 2]
print(F[2024] + F[2020] - F[2019])