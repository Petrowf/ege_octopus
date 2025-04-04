import sys
sys.setrecursionlimit(3000)
a={}
def F(n):
    global a
    if n == 1:
        return 1
    elif n == 2:
        return  2
    else:
        if(n not in a.keys()):
            a[n] = n * (n-1) + F(n-1) + F(n-2)
        return a[n]

print((F(2023)-F(2021) - 2*F(2020)-F(2019)))