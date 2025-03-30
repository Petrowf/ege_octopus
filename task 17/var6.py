with open("17var06.txt", encoding='utf-8') as file:
    numbers = list(map(int, file.readlines()))

cnt = 0
max_sum = 0
max100 = max([i for i in numbers if i%1000==100])

for i in range(len(numbers) - 2):
    troika = [numbers[i], numbers[i+1], numbers[i+2]]
    cnt3 = 0
    for n in troika:
        if 100 <= n <= 999:
            cnt3 += 1
    if cnt3 == 2 and sum(troika) <= max100:
        cnt += 1
        max_sum = max(max_sum, sum(troika))

print(cnt, max_sum)