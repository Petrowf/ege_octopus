#Растояние между точками
def dist(point1, point2):
    distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
    return distance

# Файл A
with open("dosrok_A.txt") as file:
    claster1 = []
    claster2 = []
    for row in file.readlines():
        row = row.replace(',', '.')
        x, y = map(float, row.split())

        # В экселе, посмотрели, что кластеры разделяет прямая y = 2
        if y > 2:
            claster1.append((x, y))
        else:
            claster2.append((x, y))

# Ищем центроиды
# Изначально полагаем центры кластеров (0, 0) и большое минимальное растояние до точек кластера
centr1 = [0, 0]
centr2 = [0, 0]
min_dist1 = 1000000000
min_dist2 = 1000000000

# Цетроид кластера 1
for point1 in claster1:
    dist_sum = 0
    for point2 in claster1:
        dist_sum += dist(point1, point2)
    if dist_sum < min_dist1:
        min_dist1 = dist_sum
        centr1 = point1

#Центроид кластера 2
for point1 in claster2:
    dist_sum = 0
    for point2 in claster2:
        dist_sum += dist(point1, point2)
    if dist_sum < min_dist2:
        min_dist2 = dist_sum
        centr2 = point1
# Среднее арифметическоецентров кластеров
sr_x = (centr1[0] + centr2[0])/2
sr_y = (centr1[1] + centr2[1])/2
#Первая строка ответа
print(abs(int(10000*sr_x)), abs(int(10000*sr_y)))

# Файл B
with open("dosrok_B.txt") as file:
    claster1 = []
    claster2 = []
    claster3 = []
    for row in file.readlines():
        row = row.replace(',', '.')
        x, y = map(float, row.split())

        # В экселе, посмотрели, что кластеры разделяет прямая y = 2
        if x < 0:
            claster1.append((x, y))
        elif y > 0:
            claster2.append((x, y))
        else:
            claster3.append((x, y))

# Ищем центроиды
# Изначально полагаем центры кластеров (0, 0) и большое минимальное растояние до точек кластера
centr1 = [0, 0]
centr2 = [0, 0]
centr3 = [0, 0]
min_dist1 = 1000000000000
min_dist2 = 1000000000000
min_dist3 = 1000000000000

# Цетроид кластера 1
for point1 in claster1:
    dist_sum = 0
    for point2 in claster1:
        dist_sum += dist(point1, point2)
    if dist_sum < min_dist1:
        min_dist1 = dist_sum
        centr1 = point1

#Центроид кластера 2
for point1 in claster2:
    dist_sum = 0
    for point2 in claster2:
        dist_sum += dist(point1, point2)
    if dist_sum < min_dist2:
        min_dist2 = dist_sum
        centr2 = point1

#Центроид кластера 3
for point1 in claster3:
    dist_sum = 0
    for point2 in claster3:
        dist_sum += dist(point1, point2)
    if dist_sum < min_dist3:
        min_dist3 = dist_sum
        centr3 = point1

# Среднее арифметическое центров кластеров
sr_x = (centr1[0] + centr2[0] + centr3[0])/3
sr_y = (centr1[1] + centr2[1] + centr3[1])/3

#Вторая строка ответа
print(abs(int(10000*sr_x)), abs(int(10000*sr_y)))