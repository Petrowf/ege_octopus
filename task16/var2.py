import sys
sys.setrecursionlimit(3000)
def F(n):
    if n == 1:
        return 1
    else:
        return n * F(n-1)

print((F(3000)//150 + F(2999))//F(2998))