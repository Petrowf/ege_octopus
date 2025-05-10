with open('37355.txt', encoding='utf-8') as file:
    numbers = list(map(int, file.readlines()))
    file.truncate()

cnt = 0
max_sum = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        para = [numbers[i], numbers[j]]
        if sum(para)%7 == 0:
            cnt += 1
            max_sum = max(max_sum, sum(para))
print(cnt, max_sum)
