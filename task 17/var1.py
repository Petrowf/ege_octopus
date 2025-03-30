with open("17var01.txt", encoding='utf-8') as file:
    numbers = list(map(int, file.readlines()))
cnt = 0
max_sum = 0

for i in range(len(numbers)-1):
    if (numbers[i]%27 == min(numbers)) or (numbers[i+1]%27 == min(numbers)):
        cnt +=1
        max_sum = max(max_sum, numbers[i] + numbers[i+1])

print(cnt, max_sum)
