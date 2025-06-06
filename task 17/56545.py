with open("56545.txt", encoding='utf-8') as file:
    numbers = list(map(int, file.readlines()))

min7 = min([n for n in numbers if abs(n)%10 == 7])
cnt = 0
max_sum = 0

for i in range(len(numbers) - 1):
    para = [numbers[i], numbers[i+1]]
    cnt_7 = 0
    if para[0] % 7 == 0:
        cnt_7 += 1
    if para[1] % 7 == 0:
        cnt_7 += 1
    if (abs(para[0])%10 == abs(para[1])%10) and (cnt_7 == 1) and (para[0]**2 + para[1]**2 <= min7**2):
        cnt += 1
        max_sum = max(max_sum, para[0]**2 + para[1]**2)

print(cnt, max_sum)
