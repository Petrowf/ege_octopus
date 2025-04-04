with open("17var13.txt", encoding='utf-8') as file:
    numbers = list(map(int, file.readlines()))

cnt = 0
max_sum = 0

for i in range(len(numbers)-1):
    para = [numbers[i], numbers[i+1]]
    cnt_kv = 0
    # Проверка на полный квадрат
    if para[0] >= 0:
        if para[0]**0.5 == int(para[0]**0.5):
            cnt_kv += 1
    if para[1] >= 0:
        if para[1] ** 0.5 == int(para[1] ** 0.5):
            cnt_kv += 1
    if cnt_kv > 0:
        cnt += 11
        max_sum = max(max_sum, sum(para))
print(cnt, max_sum)