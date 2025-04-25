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
# for j in range(len(pole1d) - K, len(pole1d)):
#     print(j)
#     for k in range(j%K, j, K):
#         print(k)
#         break
# for i in range(1, M+1):
#     for j in range(len(pole1d) - K*i, len(pole1d)):
#         #print(j)
#         above = sum([pole1d[k] + pole1d[k+1] for k in range(j%K, j, K)])
#         #above2 = sum([pole1d[k] for k in range((j+1)%K, j+1, K)])
#         if above == 0:
#             print(above)
    # for j in range(K-1):
    #     if sum([pole[k][j] for k in range(0, i)]) + sum([pole[k][j+1] for k in range(0, i)]) == 0:
    #         print(i, j)
