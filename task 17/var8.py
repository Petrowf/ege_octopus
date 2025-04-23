with open("17var08.txt", encoding='utf-8') as file:
    numbers = list(map(int, file.readlines()))

cnt = 0
min_sum = 10000000000
min700 = min([n for n in numbers if  abs(n)%1000 == 700])

for i in range(len(numbers) - 2):
    troika = numbers[i: i+3]
    cnt5 = 0
    for n in troika:
        if 10000 <= n <= 99999:
            cnt5 += 1
    if cnt5 <= 2 and sum(troika) >= min700:
        cnt += 1
        min_sum = min(min_sum, sum(troika))

print(cnt, min_sum)