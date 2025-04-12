with open("17var09.txt", encoding ='utf-8') as file:
    numbers = list(map(int, file.readlines()))

cnt = 0
max_sum = 0
max_n = max(numbers)

for i in range(len(numbers)-1):
    para = [numbers[i], numbers[i + 1]]
    if sum(para) == max_n:
        cnt += 1
        max_sum = max(max_sum,para[0]**2+para[1]**2)
print(cnt,max_sum)