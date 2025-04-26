with open("26var01.txt") as file:
    N, M, K = map(int, file.readline().split())
    pole = [[0 for j in range(K)] for i in range(M)]
    for n in range(N):
        i, j = map(int, file.readline().split())
        pole[i-1][j-1] = 1

pole1d = []
for i in range(M):
    pole1d.extend(pole[i])

columns = [0 for i in range(K)]

for i in range(len(columns)):
    for j in range(i, len(pole1d), K):
        if pole1d[j] == 0:
            columns[i] += 1
        else:
            break
max_i = 0
print(columns)
for i in range(len(columns) - 1):
    l = min(columns[i], columns[i-1])
    max_i = max(max_i, l)
for i in range(len(columns) - 1):
    l = min(columns[i], columns[i-1])
    if l == max_i:
        print(max_i, i)
print(max_i)

