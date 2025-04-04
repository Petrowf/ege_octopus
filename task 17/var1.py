with open("17var01.txt", encoding='utf-8') as file:
    numbers = list(map(int, file.readlines()))

cnt = 0
max_sum = 0
min_n = min(numbers)
for i in range(len(numbers) - 1):
    para = [numbers[i], numbers[i+1]]
    if para[0]%27 == min_n or para[1]%27 == min_n:
        cnt += 1
        max_sum = max(max_sum, sum(para))

print(cnt, max_sum)
