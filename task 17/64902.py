with open(r"C:\Users\petrowf\Downloads\17.txt", encoding='utf-8') as file:
    cnt = 0
    max_vel = 0
    numbers = list(map(int, file.readlines()))
    max238 = 0
    for n in numbers:
        if n % 1000 == 238:
            max238 = max(max238, n)

    for i in range(2, len(numbers)):
        troika = numbers[i-2: i+1]
        cnt5zn = 0
        cnt3kr = 0
        cnt5kr = 0
        for n in troika:
            if n // 10000 > 0 and n // 100000 == 0:
                cnt5zn += 1
            if n % 3 == 0:
                cnt3kr += 1
            if n % 5 ==0:
                cnt5kr += 1

        if 0 < cnt5zn < 3 and cnt3kr > cnt5kr and sum(troika) > max238:
            cnt += 1
            max_vel = max(max_vel, sum(troika))

print(cnt, max_vel)

