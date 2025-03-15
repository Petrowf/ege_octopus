def f(n):
    if n <= 10:
        return n*2
    elif n%2==0 and n>10:
        return f(n-3) - f(n-9)*2
    else:
        return f(n-2)*2 - f(n-7)

import sys
sys.setrecursionlimit(1000000)
print(f(3063))
