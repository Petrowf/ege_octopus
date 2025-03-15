n = 1195
k = 3

nk = ''
while n != 0:
    nk = str(n%k) + nk
    n = n // k
print(nk)