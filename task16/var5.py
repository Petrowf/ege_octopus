import sys
sys.setrecursionlimit(3000)


def F(n):
    if n == 1:
        return 5
    else:
        return 2*n + 1 + F(n-1)

print(F(2024) - F(2022))