import sys
sys.setrecursionlimit(100000)

def F(n):
    if n == 1:
        return 1
    else:
        return n * F(n-1)

print((F(2025)//25 + F(2024))//F(2023))